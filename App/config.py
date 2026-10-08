"""Cấu hình dùng chung cho bộ kiểm thử."""

import os


LOGIN_URL = "https://vanphongdientu.utc.edu.vn"
USERNAME = os.getenv("UTC_USERNAME", "huongnt")
PASSWORD = os.getenv("UTC_PASSWORD", "123456@utc")
WAIT_SECONDS = 15
