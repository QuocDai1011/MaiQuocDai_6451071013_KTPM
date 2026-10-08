"""Tên đăng nhập và mật khẩu không hợp lệ thì đăng nhập bị từ chối."""

from App.base.login_test_base import LoginTestBase


class TestInvalidCredentials(LoginTestBase):
    def test_ca_hai_thong_tin_khong_hop_le(self):
        self.login_page.fill_username("invalid_user_for_test")
        self.login_page.fill_password("wrong_password_for_test")
        self.login_page.submit()
        self.assert_login_error()
