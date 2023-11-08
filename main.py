import random

from selenium.webdriver.common.by import By

from Utils.ADBCMD import ADBCMD

# def babafarm(android):

# def shua15s(x, y, i):
#     print("正在点击", x, y, "第", i, "次")
#     time.sleep(0.5)
#     android.click(x, y)
#     time.sleep(2)
#     android.swipe_up()
#     time.sleep(6)
#     android.swipe_up()
#     time.sleep(5)
#     android.swipe_down()
#     time.sleep(5)
#     android.back()
#
# [shua15s(0x387, 0x4bc, i) for i in range(1)]
# [shua15s(0x379, 0x578, i) for i in range(8)]
# [shua15s(0x376, 0x63e, i) for i in range(3)]
# [shua15s(0x362, 0x6e6, i) for i in range(5)]
# [shua15s(0x375, 0x79b, i) for i in range(25)]

from appium import webdriver
import time

from Utils.common import Utils
from Utils.dialoghandle import DialogHandle
from Utils.popuphandle import PopupHandle

desired_caps = {
    "platformName": "Android",  # 被测手机是安卓
    "platformVersion": "13",  # 手机安卓版本
    "deviceName": "xiaomi",  # 设备名，安卓手机可以随意填写
    "appPackage": "com.taobao.taobao",  # 启动APP Package名称
    "appActivity": "com.taobao.tao.welcome.Welcome",  # 启动Activity名称
    "unicodeKeyboard": True,  # 使用自带输入法，输入中文时填True
    "resetKeyboard": True,  # 执行完程序恢复原来输入法
    "noReset": True,  # 不要重置App
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(4)
print("打开淘宝")
enterBabafarmElement = driver.find_element(By.XPATH, "//*[contains(@content-desc,'芭芭农场')]")
print("找到了芭芭农场入口")
time.sleep(3)
enterBabafarmElement.click()
print("点击了芭芭农场")

commonUtils = Utils(driver)

# 弹窗根据网速会有延时
time.sleep(random.randint(6, 10) + 5)
print("进入农场")

dialogHandle = DialogHandle(driver, commonUtils)
dialogHandle.dialog_handle()

window_size = commonUtils.get_size()
print(window_size)
driver.tap([(180/1210 * window_size[0], 1600/2700 * window_size[1])], 60)
print("点击兔子刨土收集肥料")
time.sleep(4)

popUp = PopupHandle(driver, commonUtils)
# 从下面弹窗popup
popUp.show_popup()

# 逛一逛
index_arr = popUp.glance_over_handle(commonUtils.swip_down_handle)
while index_arr and index_arr[0] < index_arr[1]:
    has_send_keys = popUp.send_keys_handle()
    if has_send_keys is False:
        index_arr = popUp.glance_over_handle(commonUtils.swip_down_handle)
        # 点击搜一搜
        popUp.click_search_search(commonUtils.swip_down_handle)
    else:
        commonUtils.swip_down_handle()



# 关闭当前操作的app，不会关闭驱动对象
# driver.close()

# count = 0  # 循环初始次数
# while count < 5:
#     driver.tap([(180, 1600)], 10)
#     count += 1
#     print("收集了{}次".format(count))
#     n = 100 * random.randint(6, 10)  # 等待收集肥料时间FF
#     time.sleep(n)
#     print("倒计时{}".format(n))

# if __name__ == "__main__":
# android = ADBCMD()  # 获得一个ADB命令实例
# babafarm(android)  # 执行芭芭农场的脚本
