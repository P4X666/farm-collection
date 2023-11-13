import time

from appium import webdriver
from selenium.webdriver.common.by import By

from Utils.common import Utils, is_array
from zhifubao.config import zhifubao_app_config


class RunZhifubaoBabaFarm:
    def __init__(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", zhifubao_app_config)
        self.utils = Utils(self.driver)
        time.sleep(4)
        print("打开支付宝")

    def open_zhifubao_baba_farm(self):
        self.utils.open_baba_farm("text")
        # enter_baba_farm_elements = self.driver.find_elements(By.XPATH, "//*[@"+attribute+",'芭芭农场']")
        # if is_array(enter_baba_farm_elements) is False:
        #     return
        # enter_baba_farm_element = None
        # for element in enter_baba_farm_elements:
        #     if element.get_attribute(attribute) == "芭芭农场":
        #         enter_baba_farm_element = element
        #         break
        # if enter_baba_farm_element is not None:
        #     print("找到了芭芭农场入口")
        #     time.sleep(3)
        #     enter_baba_farm_element.click()
        #     print("点击了芭芭农场")
