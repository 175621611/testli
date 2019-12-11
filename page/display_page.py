from typing import Tuple

from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):
    # 显示按钮
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    # 搜索按钮
    search_button: Tuple[str, str] = By.ID, "com.android.settings:id/search"
    # 搜索框
    input_text_view = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click_display()

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element(self.display_button[0], self.display_button[1]).click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_search_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.find_element(self.input_text_view).send_keys(text)
        self.input_text(self.input_text_view, text)

    def click_text_view(self):
        # self.driver.find_element(self.input_text_view).click()
        self.click(self.input_text_view)

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
