from MyObservatory.page.index_page import IndexProxy
from MyObservatory.utils import UtilsDriver


class TestMyobservatory:
    # 定义类级别的fixture初始化操作方法
    def setup_class(self):
        self.index_proxy = IndexProxy()

    # 定义类级别的fixture销毁操作方法
    def teardown_class(self):
        UtilsDriver.quit_app_driver()

    #查找 九天預報
    def test_click(self):
        self.index_proxy.find_channel('九天預報')
