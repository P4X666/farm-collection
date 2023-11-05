import subprocess
import time


class ADBCMD:
    """
    将所有ADB命令封装成一个类，更直观简洁的进行操作，和以后的使用
    """
    packageName = "com.taobao.taobao"
    activityName = "com.taobao.tao.TBMainActivity"

    def __init__(self):
        """初始化ADB,包括检查ADB是否正确安装，设备是否正确连接"""
        version = subprocess.check_output('adb version')
        if "Android Debug Bridge version" in str(version):
            print("ADB安装正常")
            print("如果手机与电脑连接完成，手机端USB调试功能打开")
            devices = subprocess.check_output('adb devices')
            if len(devices) > 28:
                print("设备", devices[26:42].decode('utf-8'), "加载成功")
            else:
                print("没有找到设备，请重新连接")
                exit(0)
        else:
            print("ADB没有正常加载，请检查环境变量或当前文件夹\n" + "Error: " + version)

    def start(self):
        """启动app"""
        subprocess.check_output("adb shell am start " + self.packageName + "/" + self.activityName)
        print("设备启动，5s后点击芭芭农场")
        time.sleep(5)
    def swipe(self, x1=500, y1=1200, x2=500, y2=600):
        """滑动屏幕"""
        subprocess.check_output("adb shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))

    def swipe_up(self):
        self.swipe(x1=500, y1=1200, x2=500, y2=600)

    def swipe_down(self):
        self.swipe(x1=500, y1=600, x2=500, y2=1200)

    def click_power(self):
        """点击电源键"""
        subprocess.check_output("adb shell input keyevent 26")

    def click(self, x, y):
        """点击屏幕中某个点"""
        subprocess.check_output("adb shell input tap " + str(x) + " " + str(y))

    def click_home(self):
        """点击Home键"""
        subprocess.check_output("adb shell input keyevent 3")

    def back(self):
        """点击返回键"""
        subprocess.check_output("adb shell input keyevent 4")
