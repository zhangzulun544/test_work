import shelve
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Testdemo():

    def setup_method(self,method):
        #复用浏览器  windos命令 ：chrome --remote-debugging-port=9222
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def test_cookie(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()

        #使用内置小型数据库shelve创建cookie键值
        with shelve.open('cookies') as db:
            cookies = db['cookie']

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        #上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "D:\测试\test_selen\test.xlsx")
        # 验证 上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "测试 est_selen est.xlsx" == filename


