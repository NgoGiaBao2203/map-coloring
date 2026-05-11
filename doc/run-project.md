> **Author:** Lê Thị Như Ý  
> **Created:** 06/05/2026  
> **Last Updated:** 10/05/2026  
> **Version:** 1.1.0

# HƯỚNG DẪN CHẠY DỰ ÁN: MAP COLORING

## 1. Danh Sách Thư Viện Sử Dụng

Dự án sử dụng các thư viện sau:

* `flask`
* `numpy`
* `opencv-python-headless`

---

## 2. Các Bước Cài Đặt Và Chạy Dự Án

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

## 3. Các Lỗi Thường Gặp Và Cách Khắc Phục

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

## 4. Ghi Chú

* Không thay đổi tên thư mục `templates` và `static`
* Đảm bảo đã cài đầy đủ thư viện trước khi chạy
* Luôn khởi động Backend trước khi truy cập giao diện web
* Khuyến khích sử dụng Visual Studio Code để chạy và debug chương trình

---

## 5. Kết Luận

Tài liệu này hướng dẫn cách cài đặt và chạy dự án Map Coloring trên môi trường local. Người dùng chỉ cần cài đầy đủ thư viện, chạy Flask Server và truy cập localhost để sử dụng hệ thống.