"""Tài khoản hợp lệ đăng nhập thành công."""

from App.base.login_test_base import LoginTestBase
from App.config import PASSWORD, USERNAME


class TestValidLogin(LoginTestBase):
    def test_dang_nhap_thanh_cong(self):
        self.login_page.fill_username(USERNAME)
        self.login_page.fill_password(PASSWORD)
        self.login_page.submit()
        self.login_page.wait_for_login_success()
