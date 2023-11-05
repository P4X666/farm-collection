import time
import random

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Utils:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_safe(self, by, value, default=None):
        try:
            element = self.driver.find_element(by, value)
            return element
        except NoSuchElementException:
            return default

    def get_size(self):  # 获取屏幕尺寸
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def back_baba_farm(self, stop=False):
        if stop is True:
            return
        time.sleep(3)
        self.driver.back()
        tutu_btn = self.find_element_safe(By.XPATH, "//*[@text,'兔兔小铺']")
        together_btn = self.find_element_safe(By.XPATH, "//*[@text,'合种']")
        if tutu_btn and together_btn:
            print("返回到了芭芭农场首页")
        else:
            self.back_baba_farm(True)

    '''向下滑动'''

    def swip_down(self):
        time.sleep(random.randint(1, 4))
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[0] * 0.73)
        y2 = int(l[0] * 0.5)
        x2 = int(l[0] * 0.35)
        self.driver.flick(x1, y1, x2, y2)
        time.sleep(4)

    def swip_down_handle(self):
        self.swip_down()
        print("第一次下滑")
        self.swip_down()
        print("第二次下滑")
        # record_btn = self.find_element_safe(By.XPATH, "//*[@text,'滑动浏览得肥料']")
        # if record_btn:
        # record_btn.parent.find_element(By.XPATH, '下单最高可得')
        self.swip_down()
        print("第三次下滑")
        self.back_baba_farm()

    '''向左滑动'''

    def swip_left(self):
        time.sleep(random.randint(1, 4))
        l = self.get_size()
        x1 = int(l[0] * 0.75)
        x2 = int(l[0] * 0.25)
        y1 = int(l[0] * 0.3)
        y2 = int(l[0] * 0.3)
        self.driver.swipe(x1, x2, y1, y2, 1000)
        time.sleep(1)
