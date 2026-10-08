# Kiểm thử đăng nhập Văn phòng điện tử UTC

Dự án dùng Python và Selenium để kiểm thử chức năng đăng nhập tại [vanphongdientu.utc.edu.vn](https://vanphongdientu.utc.edu.vn). Mã nguồn được chia thành `base`, `pages` và `tests` theo mô hình Page Object.

## Yêu cầu

- Python 3.10 trở lên.
- Google Chrome.
- Gói Python `selenium`.

Selenium Manager sẽ tự tìm hoặc tải ChromeDriver phù hợp khi chạy. Máy cần có kết nối mạng.

## Cài đặt

Mở PowerShell tại thư mục dự án và chạy:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r Requirements.txt
```

## Chạy kiểm thử

```powershell
python main.py
```

`main.py` tự tìm và chạy tất cả file có tên `test_*.py` trong `App/tests`. Chrome luôn chạy ở chế độ headless, không mở cửa sổ giao diện; mỗi test tạo một phiên trình duyệt riêng và đóng phiên đó khi kết thúc.

## Danh sách test case

Mỗi file trong `App/tests` được đặt tên theo tình huống kiểm thử:

- `test_username_required.py`: để trống tên đăng nhập.
- `test_password_required.py`: để trống mật khẩu.
- `test_invalid_credentials.py`: cả hai thông tin không hợp lệ.
- `test_both_fields_empty.py`: để trống cả tên đăng nhập và mật khẩu.
- `test_invalid_username.py`: tên đăng nhập sai, mật khẩu hợp lệ.
- `test_invalid_password.py`: tên đăng nhập hợp lệ, mật khẩu sai.
- `test_whitespace_username.py`: tên đăng nhập chỉ có dấu cách.
- `test_whitespace_password.py`: mật khẩu chỉ có dấu cách.
- `test_password_masked.py`: kiểm tra ký tự mật khẩu được che.
- `test_remember_me_default_unchecked.py`: ghi nhớ đăng nhập mặc định chưa chọn.
- `test_remember_me_toggle.py`: bật và tắt tùy chọn ghi nhớ đăng nhập.
- `test_submit_with_enter.py`: gửi form bằng phím Enter.
- `test_valid_login.py`: đăng nhập bằng tài khoản hợp lệ.

## Tài khoản kiểm thử

Mặc định chương trình dùng tài khoản đề bài: tên đăng nhập `huongnt`, mật khẩu `123456@utc`. Có thể đặt thông tin khác qua biến môi trường:

```powershell
$env:UTC_USERNAME = "ten_dang_nhap"
$env:UTC_PASSWORD = "mat_khau"
python main.py
```

Không đưa mật khẩu thật hoặc file `.env` vào Git.

## Cấu trúc

```text
.
├── main.py                         # Điểm chạy toàn bộ testcase
├── App/
│   ├── base/
│   │   ├── base_test.py            # Khởi tạo và đóng WebDriver
│   │   └── login_test_base.py      # Khởi tạo trang cho test đăng nhập
│   ├── pages/
│   │   ├── base_page.py            # Thao tác Page Object dùng chung
│   │   └── login_page.py           # Locator và thao tác trang đăng nhập
│   ├── tests/                      # Mỗi tình huống đăng nhập một file test_*.py
│   └── config.py                   # URL, tài khoản và thời gian chờ
├── .gitignore
└── README.md
```

Các trường đăng nhập được định vị theo thuộc tính `name` trong HTML: `username` và `userpwd`.
