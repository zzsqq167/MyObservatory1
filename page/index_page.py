# 首页页面对象
# 定义对象库层
from selenium.webdriver.common.by import By

from MyObservatory.base.base import BasePage,HandlePage
from MyObservatory.utils import app_swipe_find


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        #更多菜单
        self.more_element= By.CLASS_NAME,"android.widget.ImageButton"
        # 滑动的框
        self.scroll_element = By.CLASS_NAME, "android.view.ViewGroup"
        # 点击的频道
        self.channel = By.XPATH, "//android.view.ViewGroup/*[contains(@text, '{}')]"

    #查找更多按钮
    def find_more_element(self):
        return self.get_element(self.more_element)

    # 查找滑动框
    def find_scroll_element(self):
        return self.get_element(self.scroll_element)


# 定义操作层
class IndexHandle(HandlePage):
    def __init__(self):
        self.index_page = IndexPage()

    #点击更多菜单元素
    def click_more_element(self):
        self.index_page.find_more_element().click()

    # 边滑动边查找对应的频道
    def click_channel(self, channel):
        xpath = self.index_page.channel[0], self.index_page.channel[1].format(channel)
        app_swipe_find(self.index_page.driver, self.index_page.find_scroll_element(), xpath)


# 定义业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 滑动频道元素框点击对应的频道
    def find_channel(self, channel):
        self.index_handle.click_more_element()
        self.index_handle.click_channel(channel)
