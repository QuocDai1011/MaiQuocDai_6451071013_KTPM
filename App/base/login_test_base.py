"""Thiết lập chung cho các testcase đăng nhập."""

from App.base.base_test import BaseTest
from App.pages.login_page import LoginPage


class LoginTestBase(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    def assert_login_error(self):
        self.assertTrue(
            self.login_page.get_error_message(),
            "Trang cần hiển thị thông báo lỗi đăng nhập.",
        )
