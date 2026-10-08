"""Cả tên đăng nhập và mật khẩu để trống thì đăng nhập bị từ chối."""

from App.base.login_test_base import LoginTestBase


class TestBothFieldsEmpty(LoginTestBase):
    def test_ca_hai_truong_de_trong(self):
        self.login_page.fill_username("")
        self.login_page.fill_password("")
        self.login_page.submit()
        self.assert_login_error()
