# Time : 2023/4/23 16:16
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from common.logger_util import pylogger

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}



list = ['2067']
class TestJobdiva():

    # chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Chromedriver\chromeprofile"
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    def safe_clict(self, method='xpath', phrase=''):
        WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element(method, phrase))
        self.driver.find_element(method, phrase).click()

    def safe_sendkeys(self, method='xpath', phrase='', value=''):
        WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element(method, phrase))
        self.driver.find_element(method, phrase).send_keys(value)


    @pytest.mark.jobdiva_data_migration
    def test_login(self):
        pylogger.alogger.info('步骤一: 登录')
        self.driver.get("https://apn-v3-staging.hitalentech.com/login")
        self.driver.find_element('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/input').clear()
        time.sleep(1)
        self.driver.find_element('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/input').send_keys('amos.chi')
        self.driver.find_element('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div/input').clear()
        time.sleep(1)
        self.driver.find_element('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div/input').send_keys('Aa123456')
        self.driver.find_element('xpath', '//*[@id="react-app"]/div[1]/div[2]/div[1]/div/div/form/div[2]/button/span').click()
        # 加上等待时间
        WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/section/div[2]/button'))

    def edit_and_save(self):
        # 编辑按钮
        pylogger.alogger.info('点击编辑按钮')
        self.safe_clict('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/section/div[2]/button')
        # 进度条拉到底部
        self.driver.execute_script("window.scrollBy(0,1200)")
        # save按钮
        pylogger.alogger.info('点击save按钮')
        self.safe_clict('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/form/div[5]/div/button/span')

    def contacts(self):
        # contacts 按钮
        pylogger.alogger.info('等待 并点击contacts按钮')
        self.safe_clict('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[2]/span')
        # 判断是否存在联系人
        pylogger.alogger.info('判断是否存在联系人')
        try:
            self.safe_clict('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div/div[5]/div/div/div/div/div/button[2]/span')
        except:
            print('没找到该元素')
            pass

        #获取contact编辑页所有的input标签
        pylogger.alogger.info('循环点击编辑页所有的input标签')
        input_eles = self.driver.find_elements('xpath','/html/body/div[2]/div[3]/div/div//input')
        print(len(input_eles))
        i = 1
        for ele in input_eles:
            try:
                ele.click()
            except:
                print(f'erorr: 第{i}个input标签')
            i += 1
        #
        self.safe_clict(phrase='/html/body/div[2]/div[3]/div/div/div[3]/div/div/button/span')
        self.safe_clict(phrase='/html/body/div[3]/div[3]/div/div/div[3]/div[1]/div/button/span')
        self.safe_clict(phrase='/html/body/div[2]/div[3]/div/div//input[1]')
        self.safe_clict(phrase='/html/body/div[2]/div[3]/div/div/div[3]/div/div/button/span')

    def jobs(self):
        # 用三秒确定 是否存在job
        WebDriverWait(self.driver, 3, 0.5).until(lambda x: self.driver.find_element('xpath',
                                                                                    '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div'))
        #
        eles = self.driver.find_elements('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div')
        i = 1
        for i in range(1,len(eles)+1):
            print(f'第 {i} 个job:')
            # 横排长条状元素
            row = self.driver.find_elements('xpath',
                                      f'//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[{i}]/div/div/div[2]/div/div')
            for i in range(5,8):
                ele = row[i].find_element('xpath', f'./div/div/div/div/div')
                if ele.get_attribute('title'):
                    pylogger.alogger.info('点击')
                    ele.click()
                    time.sleep(2)
                    self.safe_clict(phrase='/html/body/div[2]/div[3]/div/div[4]/div/button/span')


    def service_contracts(self):
        self.driver.find_element('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[4]/span')



    @pytest.mark.jobdiva_data_migration
    @pytest.mark.parametrize('companyID', list)
    def test_find_by_companyID(self, companyID):
        pylogger.alogger.info('步骤二: 打开公司')
        self.driver.get(f"https://apn-v3-staging.hitalentech.com/companies/detail/{companyID}/0")

        self.edit_and_save()
        self.contacts()
        self.jobs()
        self.service_contracts()

if __name__ == '__main__':

    # for l in list:
    #     TestJobdiva().test_find_by_companyID(l)
    TestJobdiva().service_contracts()
