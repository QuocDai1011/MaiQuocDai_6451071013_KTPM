"""Tùy chọn ghi nhớ đăng nhập mặc định chưa được chọn."""

from App.base.login_test_base import LoginTestBase


class TestRememberMeDefaultUnchecked(LoginTestBase):
    def test_mac_dinh_chua_chon_ghi_nho(self):
        self.assertFalse(self.login_page.is_persistent_checked())
