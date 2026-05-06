# HƯỚNG DẪN CHẠY DỰ ÁN: MAP COLORING

## 1. Thông Tin Chung
*   **Tên đề tài:** Giải bài toán tô màu bản đồ (Map Coloring).
*   **Công nghệ sử dụng:** Python (Flask), JavaScript, HTML/CSS.
*   **Mục tiêu:** Xây dựng hệ thống tô màu bản đồ đảm bảo các vùng kề nhau không trùng màu.
*   **Người sử dụng:** Sinh viên, giảng viên hoặc người dùng muốn chạy thử hệ thống.

---

## 2. Yêu Cầu Hệ Thống

Để chạy được dự án, cần đảm bảo các điều kiện sau:

*   Cài đặt **Python (>= 3.10)**
*   Có **pip** để cài thư viện
*   Trình duyệt web (Chrome, Edge,...)
*   Có cài đặt **Visual Studio Code** (khuyến khích)

---

## 3. Các Bước Cài Đặt

### Bước 1: Tải source code
Mở Terminal và chạy lệnh:

    git clone <link-repository>
    cd map-coloring

---

### Bước 2: Cài đặt thư viện cần thiết

    pip install flask

Hoặc:

    python -m pip install flask

---

## 4. Chạy Chương Trình

### Bước 1: Khởi động server Flask

    python app.py

Sau khi chạy thành công, hệ thống sẽ hiển thị:

    Running on http://127.0.0.1:5000/

---

### Bước 2: Truy cập ứng dụng

Mở trình duyệt và nhập:

    http://127.0.0.1:5000

---

## 5. Cấu Trúc Thư Mục

*   **app.py:** Xử lý backend bằng Flask
*   **templates/index.html:** Giao diện chính
*   **static/script.js:** Xử lý logic frontend
*   **static/style.css:** Giao diện hiển thị

---

## 6. Mô Tả Hoạt Động

*   Người dùng truy cập giao diện web
*   Nhấn nút chạy thuật toán
*   Frontend gửi request đến backend (Flask)
*   Backend xử lý bằng thuật toán Backtracking + Heuristic
*   Kết quả trả về dạng JSON
*   Giao diện hiển thị bản đồ đã được tô màu

---

## 7. Các Lỗi Thường Gặp Và Cách Khắc Phục

### Lỗi 1: Không tìm thấy Flask

    ModuleNotFoundError: No module named 'flask'

→ Cách khắc phục:

    pip install flask

---

### Lỗi 2: Không chạy được server

→ Kiểm tra file `app.py` có đoạn sau:

    if __name__ == "__main__":
        app.run(debug=True)

---

### Lỗi 3: Không truy cập được web

→ Đảm bảo đã chạy:

    python app.py

---

### Lỗi 4: Trang web trắng

→ Kiểm tra:
*   File `templates/index.html`
*   File `script.js`

---

## 8. Ghi Chú

*   Không thay đổi tên thư mục `templates` và `static`
*   Đảm bảo đã cài đầy đủ thư viện trước khi chạy
*   Luôn chạy backend trước khi mở giao diện

---