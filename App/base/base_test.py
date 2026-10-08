"""Khởi tạo và đóng WebDriver cho mỗi test."""

import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from App.config import WAIT_SECONDS


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, WAIT_SECONDS)

    def tearDown(self):
        driver = getattr(self, "driver", None)
        if driver:
            driver.quit()
