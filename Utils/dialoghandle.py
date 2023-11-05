import time

from selenium.webdriver.common.by import By


class DialogHandle:
    def __init__(self, driver, utils):
        self.driver = driver
        self.utils = utils

    def dialog_handle(self):
        dialogElement = self.utils.find_element_safe(By.XPATH, "//*[contains(@text,'有奖励可领取哦')]", default=None)
        if dialogElement is not None:
            print("弹窗出现")
            dialogCancelTextElement = dialogElement.find_element(By.XPATH, "//*[@text,'关闭']")
            dialogCancelTextElement.click()
            print("关闭弹窗")
            time.sleep(3)
