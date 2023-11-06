import random
import time

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def find_elements_safe(parent, by, value, default=None):
    try:
        element = parent.find_elements(by, value)
        return element
    except NoSuchElementException:
        return default


class Utils:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 创建TouchAction对象，并指定driver
        self.action = ActionChains(driver)

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
        time.sleep(3)
        self.driver.back()
        if stop is True:
            return
        tutu_btn = self.find_element_safe(By.XPATH, "//*[@text,'兔兔小铺']")
        together_btn = self.find_element_safe(By.XPATH, "//*[@text,'合种']")
        if tutu_btn and together_btn:
            print("返回到了芭芭农场首页")
        else:
            self.back_baba_farm(True)

    '''向下滑动'''

    def swip_down(self, default=None):
        time.sleep(random.randint(1, 4))
        if default is None:
            wh = self.get_size()
            el_x = wh[0]
            el_y = wh[1]
            self.driver.swipe(int(852 / 720 * el_x), int(1661 / 1280 * el_y), int(852 / 720 * el_x),
                              int(866 / 1280 * el_y),
                              2000)
            time.sleep(4)
        else:
            self.driver.scroll(default[0], default[1], 2000)

    def swip_down_handle(self):
        listview_wrap = self.find_element_safe(By.CLASS_NAME, "android.widget.ListView")
        if listview_wrap is None:
            print("没有找到列表，也就没办法下滑")

        listview = find_elements_safe(listview_wrap, By.CLASS_NAME, "android.view.View")
        if listview is not None:
            print("listview 的长度", len(listview))
            self.swip_down([listview[3], listview[2]])
            print("第一次下滑")
            self.swip_down([listview[5], listview[4]])
            print("第二次下滑")
            self.swip_down([listview[5], listview[4]])
            print("第三次下滑")
        else:
            self.swip_down()
            print("第一次下滑")
            self.swip_down()
            print("第二次下滑")
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
