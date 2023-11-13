zhifubao_start_activity_path = "com.eg.android.AlipayGphone.AlipayLogin"

zhifubao_app_config = {
    "platformName": "Android",  # 被测手机是安卓
    "platformVersion": "13",  # 手机安卓版本
    "deviceName": "xiaomi",  # 设备名，安卓手机可以随意填写
    "appPackage": "com.eg.android.AlipayGphone",  # 启动APP Package名称
    "appActivity": zhifubao_start_activity_path,  # 启动Activity名称
    # "appActivity": "com.taobao.tao.welcome.TBMainActivity",  # 启动Activity名称 默认首页
    # "appActivity": "com.taobao.themis.container.app.TMSActivity",  # 跳转到芭芭农场首页
    "unicodeKeyboard": True,  # 使用自带输入法，输入中文时填True
    "resetKeyboard": True,  # 执行完程序恢复原来输入法
    "noReset": True,  # 不要重置App
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2"
}
