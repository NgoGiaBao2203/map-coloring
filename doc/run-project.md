> **Author:** Lê Thị Như Ý  
> **Created:** 06/05/2026  
> **Last Updated:** 10/05/2026  
> **Version:** 1.1.0

# HƯỚNG DẪN CHẠY DỰ ÁN: MAP COLORING

## 1. Thông Tin Chung

* **Tên đề tài:** Giải bài toán tô màu bản đồ (Map Coloring) bằng thuật toán Backtracking kết hợp Heuristic.
* **Mục tiêu:** Xây dựng hệ thống tô màu bản đồ sao cho các vùng kề nhau không trùng màu.
* **Công nghệ sử dụng:** Python (Flask), JavaScript, HTML/CSS.
* **Môi trường phát triển:** Visual Studio Code.
* **Người thực hiện tài liệu:** Lê Thị Như Ý.

---

## 2. Yêu Cầu Hệ Thống

Để chạy được dự án, máy tính cần đáp ứng các yêu cầu sau:

* Đã cài đặt **Python >= 3.10**
* Có sẵn **pip** để cài thư viện Python
* Có cài đặt **Visual Studio Code** (khuyến khích)
* Có trình duyệt web (Chrome, Edge,...)

---

## 3. Danh Sách Thư Viện Sử Dụng

Dự án sử dụng các thư viện sau:

* `flask`
* `numpy`
* `opencv-python-headless`

---

## 4. Các Bước Cài Đặt Và Chạy Dự Án

### Bước 1: Clone source code

Mở Terminal và chạy lệnh:

```bash
git clone <link-repository>
cd map-coloring
```

---

### Bước 2: Cài đặt thư viện

Cài đặt nhanh bằng file `libs.txt`:

```bash
pip install -r libs.txt
```

Hoặc cài từng thư viện:

```bash
pip install flask
pip install numpy
pip install opencv-python-headless
```

Nếu lệnh `pip` không hoạt động, dùng:

```bash
python -m pip install -r libs.txt
```

---

### Bước 3: Kiểm tra file `libs.txt`

Đảm bảo file `libs.txt` có nội dung:

```txt
flask
numpy
opencv-python-headless
```

---

### Bước 4: Chạy chương trình

Khởi động Flask Server:

```bash
python app.py
```

Hoặc:

```bash
py app.py
```

Sau khi chạy thành công, Terminal sẽ hiển thị:

```bash
* Running on http://127.0.0.1:5000
```

---

### Bước 5: Truy cập ứng dụng

Mở trình duyệt và truy cập:

```txt
http://127.0.0.1:5000
```

---

## 5. Cấu Trúc Thư Mục Dự Án

| Thư mục / File | Chức năng |
|---|---|
| `app.py` | Xử lý Backend Flask |
| `solver.py` | Thuật toán Backtracking + Heuristic |
| `image_processor.py` | Xử lý ảnh bản đồ |
| `templates/index.html` | Giao diện chính |
| `static/script.js` | Logic frontend và animation |
| `static/style.css` | Thiết kế giao diện |
| `libs.txt` | Danh sách thư viện cần cài |
| `doc/run-project.md` | Tài liệu hướng dẫn chạy dự án |

---

## 6. Quy Trình Hoạt Động Hệ Thống

* Người dùng truy cập giao diện web
* Hệ thống tải dữ liệu bản đồ
* Người dùng nhấn nút chạy thuật toán
* Frontend gửi request đến Flask Backend
* Backend xử lý thuật toán Backtracking kết hợp Heuristic
* Kết quả trả về dưới dạng JSON
* Giao diện hiển thị quá trình tô màu bằng animation

---

## 7. Các Lỗi Thường Gặp Và Cách Khắc Phục

### Lỗi 1: Không tìm thấy Flask

```bash
ModuleNotFoundError: No module named 'flask'
```

→ Cách khắc phục:

```bash
pip install flask
```

---

### Lỗi 2: Không tìm thấy OpenCV

```bash
ModuleNotFoundError: No module named 'cv2'
```

→ Cách khắc phục:

```bash
pip install opencv-python-headless
```

---

### Lỗi 3: Không tìm thấy NumPy

```bash
ModuleNotFoundError: No module named 'numpy'
```

→ Cách khắc phục:

```bash
pip install numpy
```

---

### Lỗi 4: Không chạy được Flask Server

→ Kiểm tra file `app.py` có đoạn:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

---

### Lỗi 5: Không truy cập được website

→ Đảm bảo đã chạy lệnh:

```bash
python app.py
```

---

### Lỗi 6: Trang web trắng hoặc không hiển thị dữ liệu

→ Kiểm tra:

* File `templates/index.html`
* File `static/script.js`
* Flask API có hoạt động hay không

---

### Lỗi 7: Lệnh `pip install -r libs.txt` không hoạt động

→ Kiểm tra:

* File `libs.txt` có đúng tên không
* Đang mở Terminal đúng thư mục dự án chưa

Kiểm tra bằng lệnh:

```bash
dir
```

Hoặc:

```bash
ls
```

---

## 8. Ghi Chú

* Không thay đổi tên thư mục `templates` và `static`
* Đảm bảo đã cài đầy đủ thư viện trước khi chạy
* Luôn khởi động Backend trước khi truy cập giao diện web
* Khuyến khích sử dụng Visual Studio Code để chạy và debug chương trình

---

## 9. Kết Luận

Tài liệu này hướng dẫn cách cài đặt và chạy dự án Map Coloring trên môi trường local. Người dùng chỉ cần cài đầy đủ thư viện, chạy Flask Server và truy cập localhost để sử dụng hệ thống.