"""Nhấn Enter trong ô mật khẩu gửi form đăng nhập."""

from App.base.login_test_base import LoginTestBase


class TestSubmitWithEnter(LoginTestBase):
    def test_enter_gui_form_va_nhan_loi_tai_khoan_sai(self):
        self.login_page.fill_username("invalid_user_for_test")
        self.login_page.fill_password("wrong_password_for_test")
        self.login_page.submit_with_enter()
        self.assert_login_error()
