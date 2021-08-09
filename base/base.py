# 获取元素对象
from selenium.webdriver.support.wait import WebDriverWait
from MyObservatory.utils import UtilsDriver

# 基础-获取元素对象
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_app_driver()  # 浏览器驱动对象，隐式等待

    def get_element(self, lacation):  # 找到元素，
        # 显示等待
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*lacation))
        return element


# 基础-对元素对象进行操作
class HandlePage:
    def input_text(self, element, text):
        """

        :param element: 元素对象
        :param text: 输入的文本内容
        :return:
        """
        element.clear()
        element.send_keys(text)