"""Tên đăng nhập sai cùng mật khẩu hợp lệ thì đăng nhập bị từ chối."""

from App.base.login_test_base import LoginTestBase
from App.config import PASSWORD


class TestInvalidUsername(LoginTestBase):
    def test_ten_dang_nhap_khong_dung(self):
        self.login_page.fill_username("invalid_user_for_test")
        self.login_page.fill_password(PASSWORD)
        self.login_page.submit()
        self.assert_login_error()
