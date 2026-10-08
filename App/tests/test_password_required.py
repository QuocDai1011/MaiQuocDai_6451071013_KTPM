"""Mật khẩu để trống, tên đăng nhập hợp lệ thì đăng nhập bị từ chối."""

from App.base.login_test_base import LoginTestBase
from App.config import USERNAME


class TestPasswordRequired(LoginTestBase):
    def test_password_de_trong(self):
        self.login_page.fill_username(USERNAME)
        self.login_page.fill_password("")
        self.login_page.submit()
        self.assert_login_error()
