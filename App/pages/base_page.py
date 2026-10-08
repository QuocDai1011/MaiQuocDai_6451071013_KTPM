"""Các thao tác Selenium dùng chung cho Page Object."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from App.config import WAIT_SECONDS


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_SECONDS)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
