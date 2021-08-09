#定义驱动对象
import time
from appium import webdriver as webdriverapp
from selenium.webdriver.common.by import By


class UtilsDriver:

    _app_driver = None  # 移动端

    #创建移动端驱动
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            des_cap = {
                'platformName': 'android',  # 表示手机系统
                'platformVersion': '7.1.2',  # 表示手机系统版本
                'deviceName': 'emulator-5554',  # 表示设备id名称（如果只有一个系统可以用****代替）
                'appPackage': 'hko.MyObservatory_v1_0',  # 表示app包名
                'appActivity': '.hko.homepage.Homepage2Activity',  # 表示app界面名
                'resetKeyboard': True,  # 重置设备输入键盘（才可以输入中文）
                'unicodeKeyboard': True,  # 采用unicode编码格式（才可以输入中文）
                'noReset': True  # 判断是否非首次打开，记住app的session
            }
            cls._app_driver=webdriverapp.Remote('http://localhost:4723/wd/hub',des_cap)
        return cls._app_driver

    #退出移动端驱动
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls.get_app_driver().quit()
            cls._app_driver=None

#封装-判断元素是否存在
def is_exist(driver,text):
    """
    :param driver: 浏览器驱动
    :param text: 定位元素的文本内容
    :return:
    """
    xpath="//*[contains(text(),'{}')]".format(text)
    try:
        time.sleep(2)
        return driver.find_element(By.XPATH,xpath)

    except Exception as e:
        return False

# 定义app中边滑动边查找的方法
def app_swipe_find(driver, element, target_ele):
    """
    :param driver: 表示的是app的驱动
    :param element: 表示的滑动的元素对象
    :param target_ele: 表示的是要查找的元素的定位的值
    :return:
    """
    location = element.location  # 获取元素的坐标点位置
    x = location["x"]  # 获取坐标点X的值
    y = location["y"]  # 获取坐标点y的值
    size = element.size
    width = size["width"]
    height = size["height"]
    start_x = x + width*0.3
    start_y = y+ height*0.4
    end_y = y + height * 0.9
    while True:
        page_source = driver.page_source
        try:
            time.sleep(1)
            driver.find_element(*target_ele).click()
            return True
        except Exception as e:
            driver.swipe(start_x, start_y, start_x, end_y, duration=1500)
        if page_source == driver.page_source:
            print("已滑屏到最后的页面，没有找到对应频道！")
            return False


