"""Mật khẩu sai cùng tên đăng nhập hợp lệ thì đăng nhập bị từ chối."""

from App.base.login_test_base import LoginTestBase
from App.config import USERNAME


class TestInvalidPassword(LoginTestBase):
    def test_mat_khau_khong_dung(self):
        self.login_page.fill_username(USERNAME)
        self.login_page.fill_password("wrong_password_for_test")
        self.login_page.submit()
        self.assert_login_error()
