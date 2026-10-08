"""Tên đăng nhập chỉ chứa dấu cách không được chấp nhận."""

from App.base.login_test_base import LoginTestBase
from App.config import PASSWORD


class TestWhitespaceUsername(LoginTestBase):
    def test_username_chi_co_khoang_trang(self):
        self.login_page.fill_username("   ")
        self.login_page.fill_password(PASSWORD)
        self.login_page.submit()
        self.assert_login_error()
