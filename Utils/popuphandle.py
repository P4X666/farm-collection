import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Utils.common import Utils


class PopupHandle:
    def __init__(self, driver: WebDriver, utils: Utils):
        self.driver = driver
        self.utils = utils

    def show_popup(self):
        collectionFertilizerElement = self.driver.find_element(By.XPATH, "//*[contains(@text,'集肥料')]")
        print("找到了 集肥料 按钮")
        collectionFertilizerElement.click()
        print("点击了 集肥料 按钮")
        time.sleep(3)

    def click_search_search(self, callback):
        print("click_search_search")
        findYouLikeProductElement = self.utils.find_element_safe(By.XPATH, "//*[contains(@text,'搜一搜')]",
                                                                 default=None)
        if findYouLikeProductElement is None:
            return
        print("找到了搜一搜")
        button = findYouLikeProductElement.parent.find_element(By.XPATH, "//*[contains(@text,'去完成')]")
        button.click()
        print("点击搜一搜去看视频")
        time.sleep(3)
        # 搜一搜
        self.send_keys_handle()
        callback()

    # 每日签到
    def sign_in(self):
        button = self.utils.find_element_safe(By.XPATH, "//*[@text,'去签到']")
        if button is not None:
            button.click()
            time.sleep(3)

    # 浏览视频
    def glance_over_handle(self, callback):
        print("glance_over_handle")
        self.sign_in()
        element_path = "//*[contains(@text,'浏览15秒得')]/../.."
        glance_over_element = self.utils.find_element_safe(By.XPATH, element_path, default=None)
        if glance_over_element is None:
            print("浏览15秒得 没有找到")
            glance_over_element = self.utils.find_element_safe(By.XPATH, "//*[contains(@text,'搜一搜')]", default=None)
            if glance_over_element is None:
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

        search_title = self.utils.find_element_safe(By.XPATH, "//*[@text,'搜索']", default=None)
        if search_title is not None:
            self.send_keys_handle()
        callback()
        return [int(index_arr[0]), int(index_arr[1])]

    # input 框输入查询内容
    def send_keys_handle(self):
        print("send_keys_handle")

        searchBtn = self.utils.find_element_safe(By.XPATH, "//*[@text,'搜索']", default=None)

        if searchBtn is None:
            return False
        print("找到了 搜索 按钮")
        searchBtn.click()
        searchInput = self.utils.find_element_safe(By.CLASS_NAME, 'android.widget.EditText', default=None)
        if searchInput is None:
            return False
        search_text = searchInput.get_attribute('text')
        if search_text:
            print("存在搜索内容")
        else:
            searchInput.click()
            searchInput.send_keys('python')
            print("输入python")

            searchBtn.click()
            print("点击搜索")
        return True
