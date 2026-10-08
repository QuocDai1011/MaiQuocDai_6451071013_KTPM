"""Page Object cho trang đăng nhập UTC."""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from App.config import LOGIN_URL
from App.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "userpwd")
    PERSISTENT = (By.NAME, "persistent")
    PERSISTENT_LABEL = (By.CSS_SELECTOR, 'label.check[for="persistent"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, "form .error")

    def open(self):
        self.driver.get(LOGIN_URL)
        self.wait_visible(self.USERNAME)
        self.wait_visible(self.PASSWORD)

    def fill_username(self, value):
        field = self.wait_visible(self.USERNAME)
        field.clear()
        if value:
            field.send_keys(value)

    def fill_password(self, value):
        field = self.wait_visible(self.PASSWORD)
        field.clear()
        if value:
            field.send_keys(value)

    def submit(self):
        self.wait_visible(self.USERNAME).submit()

    def submit_with_enter(self):
        self.wait_visible(self.PASSWORD).send_keys(Keys.ENTER)

    def get_error_message(self):
        return self.wait_visible(self.ERROR_MESSAGE).text.strip()

    def is_persistent_checked(self):
        return self.wait_present(self.PERSISTENT).is_selected()

    def toggle_persistent(self):
        self.wait_visible(self.PERSISTENT_LABEL).click()

    def wait_for_login_success(self):
        self.wait.until(lambda driver: not driver.find_elements(*self.USERNAME))
