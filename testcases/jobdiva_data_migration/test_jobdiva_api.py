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

def save_clict():



list = ['2067']
class TestJobdiva():
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Chromedriver\chromeprofile"
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
        WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/section/div[2]/button'))
        self.driver.find_element('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/section/div[2]/button').click()
        # 进度条拉到底部
        self.driver.execute_script("window.scrollBy(0,1200)")
        # save按钮
        pylogger.alogger.info('点击save按钮')
        WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/form/div[5]/div/button/span'))
        self.driver.find_element('xpath','//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/form/div[5]/div/button/span').click()

    def contacts(self):
        # contacts 按钮
        pylogger.alogger.info('等待 并点击contacts按钮')
        WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element('xpath',
                                                                                    '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[2]/span'))
        self.driver.find_element('xpath', '//*[@id="react-app"]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[2]/span').click()
        # 判断是否存在联系人
        pylogger.alogger.info('判断是否存在联系人')
        try:
            WebDriverWait(self.driver, 8, 0.5).until(lambda x: self.driver.find_element('xpath',
                                                                                    '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div[1]/div/div[2]/div/div/div/div'))

            self.driver.find_element('xpath',
                                     '//*[@id="react-app"]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div/div[5]/div/div/div/div/div/button[2]/span').click()
        except:
            print('没找到该元素')
            pass



    @pytest.mark.jobdiva_data_migration
    @pytest.mark.parametrize('companyID', list)
    def test_find_by_companyID(self, companyID):
        pylogger.alogger.info('步骤二: 打开公司')
        self.driver.get(f"https://apn-v3-staging.hitalentech.com/companies/detail/{companyID}/0")

        self.edit_and_save()
        self.contacts()



if __name__ == '__main__':
    #TestJobdiva().test_login()
    try:
        TestJobdiva().test_find_by_companyID('2067')
    except:
        TestJobdiva().driver.find_element('xpath',
                                 '//*[@id="react-app"]/div[1]/div[2]/div[1]/div/div/form/div[2]/button/span').click()
    #TestJobdiva().contacts()