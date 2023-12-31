import time

from appium import webdriver

from Utils.common import Utils
from taobao.config import taobao_app_config, taobao_baba_farm_activity, taobao_search_fuli_search_activity
from taobao.dialoghandle import DialogHandle
from taobao.popuphandle import PopupHandle
import subprocess


# 点击兔子收集肥料
def click_rabbit():
    time.sleep(2)
    # 定义adb命令列表
    # adb_commands = [
    #     'adb shell input tap 180 1600',
    #     'adb kill-server'
    # ]
    # # 创建子进程执行adb命令
    # processes = []
    # for cmd in adb_commands:
    #     process = subprocess.Popen(cmd, shell=True)
    #     processes.append(process)
    #
    # # 等待所有子进程执行完毕
    # for process in processes:
    #     process.wait()
    # 要执行的adb命令
    adb_command = 'adb shell input tap 180 1600'

    # 使用subprocess模块调用adb命令
    subprocess.run(adb_command, shell=True)
    # 要执行的adb命令
    # adb_command_kill = 'adb kill-server'

    # 使用subprocess模块调用adb命令
    # subprocess.run(adb_command_kill, shell=True)
    print("点击兔子收集肥料")
    time.sleep(2)


class RunTaobaoBabaFarm:
    def __init__(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", taobao_app_config)
        self.utils = Utils(self.driver)
        self.dialogHandle = DialogHandle(self.driver, self.utils)
        self.popUp = PopupHandle(self.driver, self.utils)
        time.sleep(4)
        print("打开淘宝")

    success_flag = False

    def open_baba_farm(self):
        def callback():
            self.success_flag = True

        self.utils.open_baba_farm("content-desc", taobao_baba_farm_activity, callback)
        if self.success_flag is False:
            return
        print("成功打开芭芭农场")

        click_rabbit()

        self.popUp.show_popup()
        self.glance_over_15s()

    # 浏览15s
    def glance_over_15s(self):
        popUp = self.popUp
        commonUtils = self.utils
        index_arr = popUp.glance_over_handle()
        while index_arr and index_arr[0] < index_arr[1]:
            print("当前的activity", self.driver.current_activity)
            if self.driver.current_activity == taobao_search_fuli_search_activity:
                popUp.send_keys_handle()
            commonUtils.swip_down_handle()
            index_arr = popUp.glance_over_handle()
            commonUtils.swip_down_handle()
