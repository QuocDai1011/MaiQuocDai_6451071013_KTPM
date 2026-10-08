"""Tên đăng nhập để trống, mật khẩu hợp lệ thì đăng nhập bị từ chối."""

from App.base.login_test_base import LoginTestBase
from App.config import PASSWORD


class TestUsernameRequired(LoginTestBase):
    def test_username_de_trong(self):
        self.login_page.fill_username("")
        self.login_page.fill_password(PASSWORD)
        self.login_page.submit()
        self.assert_login_error()
