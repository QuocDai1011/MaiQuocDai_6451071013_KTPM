"""Mật khẩu chỉ chứa dấu cách không được chấp nhận."""

from App.base.login_test_base import LoginTestBase
from App.config import USERNAME


class TestWhitespacePassword(LoginTestBase):
    def test_password_chi_co_khoang_trang(self):
        self.login_page.fill_username(USERNAME)
        self.login_page.fill_password("   ")
        self.login_page.submit()
        self.assert_login_error()
