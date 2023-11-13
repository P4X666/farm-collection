import time

from selenium.webdriver.common.by import By


class DialogHandle:
    def __init__(self, driver, utils):
        self.driver = driver
        self.utils = utils

    def dialog_handle(self):
        dialogCancelTextElement = self.utils.find_element_safe(By.XPATH, "//*[contains(@text,'关闭')]", default=None)
        if dialogCancelTextElement is not None:
            dialogCancelTextElement.click()
            print("关闭弹窗")
            time.sleep(3)
