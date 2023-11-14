import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Utils.common import Utils


class PopupHandle:
    def __init__(self, driver: WebDriver, utils: Utils):
        self.driver = driver
        self.utils = utils

    def show_popup(self):
        collectionFertilizerElements = self.utils.find_elements_safe(By.XPATH, "//*[@text,'集肥料']")
        collectionElements = list(filter(lambda ele: ele.get_attribute("text") == "集肥料", collectionFertilizerElements))
        if self.utils.is_array(collectionElements) is False or len(collectionElements) == 0:
            print("没有找到 集肥料 按钮，退出")
            return
        print("找到了 集肥料 按钮")
        collectionElements[0].click()
        print("点击了 集肥料 按钮")
        time.sleep(3)

    # 每日签到
    def sign_in(self):
        button = self.utils.find_element_safe(By.XPATH, "//*[@text,'去签到']")
        if button is not None:
            button.click()
            time.sleep(3)

    def get_glance_over_flag(self):
        element_path = "//*[contains(@text,'浏览15秒得')]/../.."
        glance_over_element = self.utils.find_element_safe(By.XPATH, element_path, default=None)
        if glance_over_element is None:
            return self.utils.find_element_safe(By.XPATH, "//*[contains(@text,'搜一搜')]", default=None)
        return glance_over_element

    # 浏览视频
    def glance_over_handle(self):
        time.sleep(1)
        print("glance_over_handle")
        self.sign_in()
        glance_over_element = self.get_glance_over_flag()
        if glance_over_element is None:
            print("浏览15秒得 没有找到")
            return
        text_node_path = "//*[contains(@text,'浏览15秒得')]/../../android.widget.TextView"
        text_node = self.utils.find_element_safe(By.XPATH, text_node_path, default=None)
        if text_node is None:
            print("没有找到内容")
            return
        text: str = text_node.get_attribute('text')  # type: ignore
        print("找到了" + text)
        button = glance_over_element.parent.find_element(By.XPATH, "//*[contains(@text,'去完成')]")
        button.click()
        print("点击去完成浏览")
        time.sleep(3)
        index_arr = text.split('(')[1].split(')')[0].split('/')
        return [int(index_arr[0]), int(index_arr[1])]

    # input 框输入查询内容
    def send_keys_handle(self):
        print("send_keys_handle")
        searchBtn = self.utils.find_element_safe(By.XPATH, "//*[@text,'搜索']", default=None)
        if searchBtn is None:
            return
        print("找到了 搜索 按钮")
        searchInput = self.utils.find_element_safe(By.CLASS_NAME, 'android.widget.EditText', default=None)
        if searchInput is None:
            return
        search_text = searchInput.get_attribute('text')
        if search_text:
            print("存在搜索内容")
        else:
            searchInput.click()
            searchInput.send_keys('python')
            print("输入python")

        searchBtn.click()
        time.sleep(1)
        print("点击搜索")
