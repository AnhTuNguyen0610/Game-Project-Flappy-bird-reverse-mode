
# 🐦 Flappy Bird - Reverse Mode
Một phiên bản sáng tạo của trò chơi Flappy Bird: **Thay vì điều khiển chim né ống**, bạn sẽ **điều khiển ống để né chim**!  
Game được viết bằng Python với thư viện **Pygame**, sử dụng mô hình **Lập trình Hướng Đối Tượng (OOP)** rõ ràng, dễ bảo trì và mở rộng.
## 🎮 Gameplay
- Nhấn `SPACE` để bắt đầu.
- Dùng `↑` và `↓` để điều khiển ống di chuyển lên/xuống tránh chim.
- Nhấn `P` để tạm dừng / tiếp tục.
- Nhấn `ESC` để thoát.
- Game tăng độ khó sau mỗi 5 điểm.
- Điểm cao nhất được lưu lại tự động.
---
## 🧱 Cấu trúc chương trình
Dự án được chia thành các thành phần độc lập theo mô hình OOP, mỗi phần phụ trách một vai trò riêng:
### `main.py`
- Điểm khởi đầu của game.
- Khởi tạo game, vòng lặp chính, điều hướng giữa các trạng thái (menu, chơi, kết thúc, tạm dừng).
### `constants.py`
- Chứa các hằng số như kích thước cửa sổ, tốc độ, màu sắc, font, v.v.
### `assetmanager.py`
- Tải và quản lý tài nguyên (ảnh, âm thanh, font) một cách tập trung.
### `bird.py`
- Đại diện cho **chim**.
- Chim rơi tự do và bay lên theo nhịp cố định.
- Chim xuất hiện từ bên phải và di chuyển sang trái.
- Tự động spawn định kỳ và bị xóa khi ra khỏi màn hình.
### `pipe.py`
- Đại diện cho **ống** do người chơi điều khiển.
- Có thể di chuyển lên hoặc xuống.
- Kiểm tra va chạm với chim.
### `ground.py` & `cloud.py`
- Tạo hiệu ứng nền (đất và mây) để tăng tính trực quan và sinh động.
- Tự cuộn theo thời gian tạo cảm giác chuyển động.
### `score_manager.py`
- Theo dõi điểm hiện tại và điểm cao nhất.
- Tăng điểm khi né chim thành công.
- Lưu điểm cao nhất vào file `high_score.txt`.
### `stage_manager.py`
- Quản lý trạng thái tổng thể của game:
  - `menu`, `playing`, `paused`, `game_over`
- Cho phép chuyển trạng thái dễ dàng.
### `collision_detector.py`
- Kiểm tra va chạm giữa ống và chim.
- Nếu có va chạm → chuyển sang trạng thái kết thúc.
---
## 📁 Cấu trúc thư mục
```bash
flappy-bird-reverse/
├── assets/                # Hình ảnh
├── sound/                 # Âm thanh
├── bird.py                # Chim (đối tượng chuyển động cần tránh)
├── pipe.py                # Ống (người chơi điều khiển)
├── cloud.py               # Mây (trang trí nền)
├── ground.py              # Đất (hiệu ứng nền)
├── score_manager.py       # Quản lý điểm
├── stage_manager.py       # Quản lý trạng thái game
├── collision_detector.py  # Xử lý va chạm
├── assetmanager.py        # Tải và lưu tài nguyên
├── constants.py           # Các hằng số toàn cục
├── main.py                # Vòng lặp chính của game
├── high_score.txt         # File lưu điểm cao
└── README.md


