"""Nhãn ghi nhớ đăng nhập bật và tắt được checkbox tương ứng."""

from App.base.login_test_base import LoginTestBase


class TestRememberMeToggle(LoginTestBase):
    def test_bat_tat_ghi_nho_dang_nhap(self):
        initial_state = self.login_page.is_persistent_checked()

        self.login_page.toggle_persistent()
        self.assertNotEqual(self.login_page.is_persistent_checked(), initial_state)

        self.login_page.toggle_persistent()
        self.assertEqual(self.login_page.is_persistent_checked(), initial_state)
