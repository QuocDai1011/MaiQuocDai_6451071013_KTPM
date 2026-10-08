"""Trường mật khẩu phải dùng kiểu password để che ký tự nhập."""

from App.base.login_test_base import LoginTestBase
from App.pages.login_page import LoginPage


class TestPasswordMasked(LoginTestBase):
    def test_truong_mat_khau_duoc_che(self):
        password_field = self.login_page.wait_visible(LoginPage.PASSWORD)
        self.assertEqual(password_field.get_attribute("type"), "password")
