import os, sys

sys.path.append(os.getcwd())

import base.base_driver
from page.network_page import NetworkPage


class TestNetwork:
    def setup(self):
        self.driver = base.base_driver.init_driver()
        self.network_page = NetworkPage(self.driver)

    def test_mobile_network_2g(self):
        # xxxx
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_2g_network()

    def test_mobile_network_3g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_3g_network()
