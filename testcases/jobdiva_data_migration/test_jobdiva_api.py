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



list = ['20','24','2067']
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
        pylogger.alogger.info('{:-^50}'.format('公司详情页'))
        # 编辑按钮
        pylogger.alogger.info('编辑公司')
        self.safe_clict('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/section/div[2]/button')
        # 进度条拉到底部
        self.driver.execute_script("window.scrollBy(0,1200)")
        # save按钮
        pylogger.alogger.info('点击cancel按钮')
        self.safe_clict('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/form/div[5]/button/span')

    def contacts(self):
        pylogger.alogger.info('{:-^30}'.format('客户联系人'))
        # contacts 按钮
        pylogger.alogger.info('等待页面加载 并点击contacts按钮')
        self.safe_clict('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[2]/span')

        try:
            pylogger.alogger.info('判断是否存在联系人 并点击编辑按钮')
            self.safe_clict('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div/div[5]/div/div/div/div/div/button[2]/span')
        except:
            print('可能没有客户联系人')


        #获取contact编辑页所有的input标签
        pylogger.alogger.info('循环点击编辑页所有的input标签')
        input_eles = self.driver.find_elements('xpath','/html/body/div[2]/div[3]/div/div//input')
        i = 1
        for ele in input_eles:
            try:
                ele.click()
            except:
                print(f'erorr: 第{i}个input标签')
            i += 1
        #退出编辑
        self.safe_clict(phrase='/html/body/div[2]/div[3]/div/div/div[3]/div/button/span')


    def jobs(self):
        pylogger.alogger.info('{:-^30}'.format('jobs列表'))
        self.driver.find_element('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[3]/span').click()

        try:

            # 用8秒确定 是否存在job
            WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element('xpath',
                                                                                        '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div'))
        except :
            pylogger.alogger.info('可能无job')


        # jobs
        eles = self.driver.find_elements('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div')

        for ele in eles:
            pylogger.alogger.info('job: ')
            # 每个job下面的横排元素
            row = ele.find_element('xpath','./div/div/div[2]/div')
            # 每个横排元素下的列
            columns = row.find_elements('xpath', './div')
            # 遍历每个job下的第 6 7 8个列元素 点击
            for i in range(5,8):
                ele = columns[i].find_element('xpath', f'./div/div/div/div/div')
                if ele.get_attribute('title'):
                    pylogger.alogger.info(' ->>点击')
                    ele.click()
                    time.sleep(2)
                    self.safe_clict(phrase='/html/body/div[2]/div[3]/div/div[4]/div/button/span')


    def service_contracts(self):
        pylogger.alogger.info('{:-^30}'.format('合同列表'))
        self.safe_clict('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[4]/span')

        try:
            # 获取有多少合同
            WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element('xpath',
                                                                                        '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div'))
            rows = self.driver.find_elements('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div')
            if len(rows) == 0:
                raise Exception('没有合同')

            for row in rows:
                pylogger.alogger.info('{:-^16}'.format('合同'))
                pylogger.alogger.info('查看合同')
                view_contract_ele = row.find_element('xpath','./div/div/div[2]/div/div[7]/div/div/div/div/button/span')
                view_contract_ele.click()
                time.sleep(4)

                pylogger.alogger.info('退出查看合同')
                self.safe_clict(phrase='/html/body/div[2]/div[3]/div/div/div[2]/button/span')

                pylogger.alogger.info('编辑合同')
                time.sleep(2)
                edit_contract_ele = row.find_element('xpath', './div/div/div[2]/div/div[8]/div/div/div/div/div/button')
                edit_contract_ele.click()

                pylogger.alogger.info('选择日期')
                self.safe_clict(phrase='//*[@id="contractForm"]/div[4]/div[1]/div[1]/div/div/label/input')
                self.safe_clict(phrase='//*[@id="contractForm"]/div[4]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]')
                self.safe_clict(phrase='//*[@id="contractForm"]/div[4]/div[2]/div[1]/div/div/label/input')
                self.safe_clict(phrase='//*[@id="contractForm"]/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[5]/div[6]')

                pylogger.alogger.info('取消保存')
                self.safe_clict('xpath', '/html/body/div[2]/div[3]/div/div[3]/div/button/span')

        except :
            pylogger.alogger.info('可能无合同')

    def program_team(self):
        pylogger.alogger.info('{:-^30}'.format('program team'))
        self.safe_clict('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[5]/span')


        try:
            WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div/div/div/div[2]/div'))
            eles = self.driver.find_elements('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div/div/div/div[2]/div')

            for row in eles:
                pylogger.alogger.info('编辑team')
                teamName = row.find_element('xpath', './div[1]/div/div/div/div/div/button')
                teamName.click()

                pylogger.alogger.info('退出编辑team')
                self.safe_clict(phrase='/html/body/div[2]/div[3]/div/div[3]/button/span')

        except:
            pylogger.alogger.info('可能没有team')


    def note(self):
        pylogger.alogger.info('{:-^30}'.format('NOTE'))
        self.driver.find_element('xpath',
                                 '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[6]/span').click()
        pylogger.alogger.info('ok')

    def amReport(self):
        pylogger.alogger.info('{:-^30}'.format('AM Report'))
        self.driver.find_element('xpath',
                                 '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[7]/span').click()
        pylogger.alogger.info('ok')

    @pytest.mark.jobdiva_data_migration
    @pytest.mark.parametrize('companyID', list)
    def test_find_by_companyID(self, companyID):
        pylogger.alogger.info(f'步骤二: 打开公司:{companyID}')
        self.driver.get(f"https://apn-v3-staging.hitalentech.com/companies/detail/{companyID}/0")

        self.edit_and_save()
        self.contacts()
        self.jobs()
        self.service_contracts()
        self.program_team()
        self.note()
        self.amReport()

if __name__ == '__main__':

    for l in list:
        TestJobdiva().test_find_by_companyID(l)

