> **Author:** Lê Thị Như Ý
> **Created:** 07/05/2026
> **Last Updated:** 07/05/2026
> **Version:** 1.0.0

# Backend với Flask

---

## 1. Giới thiệu

Flask là một framework của Python dùng để xây dựng ứng dụng web nhẹ và đơn giản. Trong hệ thống này, Flask đóng vai trò là backend xử lý logic và giao tiếp với frontend.

---

## 2. Vai trò của Flask trong hệ thống

Flask đảm nhận các chức năng chính:

- Nhận yêu cầu (request) từ phía người dùng  
- Thực thi thuật toán tô màu bản đồ  
- Trả kết quả về cho frontend dưới dạng dữ liệu JSON  

---

## 3. Quy trình hoạt động

Quy trình hoạt động của hệ thống như sau:

1. Người dùng bấm nút “Tô màu” trên giao diện  
2. Frontend gửi request đến server Flask  
3. Flask nhận request và xử lý  
4. Thuật toán Backtracking được thực thi  
5. Kết quả được trả về dưới dạng JSON  
6. Frontend nhận dữ liệu và hiển thị màu lên bản đồ  

---

## 4. Cấu trúc cơ bản của Flask

Một ứng dụng Flask đơn giản bao gồm:

- Khai báo ứng dụng Flask  
- Định nghĩa các route (đường dẫn)  
- Xử lý request và trả response  

---

## 5. Ví dụ API

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/color', methods=['GET'])
def color_map():
    result = solve_map()  # gọi hàm xử lý thuật toán
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```

## 6. Kết luận

Flask đóng vai trò trung gian giữa giao diện người dùng và thuật toán xử lý. Nhờ Flask, hệ thống có thể nhận yêu cầu, xử lý dữ liệu và trả kết quả một cách linh hoạt và hiệu quả.