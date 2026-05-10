> **Author:** Ngô Gia Bảo
> **Created:** 05/05/2026  
> **Last Updated:** 10/05/2026  
> **Version:** 1.2.0

# LUỒNG HOẠT ĐỘNG CỦA HỆ THỐNG (SYSTEM FLOW)

Dự án Map Coloring áp dụng kiến trúc Client - Server cơ bản:

- **Client (Frontend):** `index.html`, `style.css`, `script.js` (Xử lý giao diện và hiệu ứng).
- **Server (Backend):** `app.py` (Xử lý API và chạy thuật toán AI).

---

## 1. Luồng Tương Tác Tổng Thể (User Flow)

| Bước  | Quá trình                   |    Nơi xử lý    | Chi tiết hoạt động                                                                                                                                                                                                           |
| :---: | :-------------------------- | :-------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Khởi tạo giao diện**      | Client / Server | Người dùng truy cập web. Flask (`app.py`) render file `index.html`. Giao diện hiển thị form upload và canvas trống.                                                                                                          |
| **2** | **Chọn và upload ảnh**      |   Client (JS)   | Người dùng chọn file ảnh bản đồ qua input file. `script.js` hiển thị preview ảnh gốc.                                                                                                                                        |
| **3** | **Gửi yêu cầu upload**      |   Client (JS)   | Người dùng bấm nút **"Upload & Giải"**. `script.js` gửi HTTP Request (POST) tới API (`/upload`) với FormData chứa ảnh.                                                                                                       |
| **4** | **Xử lý ảnh và thuật toán** |   Server (AI)   | Flask nhận file, lưu vào `static/uploads/`. `image_processor.py` xử lý ảnh: kiểm tra nền trắng viền đen, tìm contours, tạo đồ thị láng giềng. Sau đó `solver.py` chạy thuật toán **Backtracking + Heuristic** để tìm đáp án. |
| **5** | **Trả kết quả**             |  Server (API)   | Sau khi tìm được tập màu hợp lệ, `app.py` đóng gói kết quả thành chuỗi JSON và gửi trả về cho Frontend. Nếu lỗi (ảnh không hợp lệ), trả JSON lỗi.                                                                            |
| **6** | **Hiển thị và animation**   |   Client (JS)   | `script.js` nhận JSON, hiển thị preview, vẽ bản đồ trên canvas, dùng vòng lặp và `setTimeout()` để đổi màu từng vùng theo thứ tự steps, tạo animation.                                                                       |

---

## 2. Luồng Xử Lý Ảnh (Image Processing Flow)

Chi tiết quy trình xử lý ảnh trong **Bước 4**:

| Trình tự | Giai đoạn xử lý     | Kỹ thuật áp dụng | Mô tả chi tiết                                                                                                                    |
| :------: | :------------------ | :--------------: | :-------------------------------------------------------------------------------------------------------------------------------- |
|  **1**   | **Đọc và kiểm tra** |   OpenCV Load    | Đọc ảnh bằng `cv2.imread()`. Chuyển grayscale, kiểm tra nền trắng (>90% biên) và viền đen (>0.1% ảnh). Nếu không hợp lệ, trả lỗi. |
|  **2**   | **Threshold**       |    Binary Inv    | Áp dụng threshold để tách viền đen thành trắng, nền trắng thành đen.                                                              |
|  **3**   | **Tìm contours**    |     CV2 Find     | Sử dụng `cv2.findContours()` để tìm tất cả đường viền các vùng. Lọc bỏ nền và contours quá nhỏ (<500px).                          |
|  **4**   | **Tạo đồ thị**      |   Graph Build    | Với mỗi contour, tạo node với danh sách neighbors dựa trên bounding box overlap. Xuất dict regions với points và neighbors.       |
|  **5**   | **Debug output**    |     CV2 Draw     | Vẽ contours lên ảnh debug và lưu vào `static/debug/debug_contours.png`.                                                           |

---

## 3. Luồng Chạy Core AI (Backtracking + Heuristic Flow)

Chi tiết quy trình xử lý bên trong **Bước 4** (Solver):

| Trình tự | Giai đoạn xử lý        | Kỹ thuật áp dụng | Mô tả chi tiết                                                                                     |
| :------: | :--------------------- | :--------------- | :------------------------------------------------------------------------------------------------- |
|  **1**   | **Khởi tạo Đồ thị**    | Graph Build      | Nạp dict regions từ image_processor, chuyển thành graph với neighbors.                             |
|  **2**   | **Chọn biến**          | Heuristic        | Dùng Degree Heuristic: chọn vùng chưa gán có nhiều neighbors nhất.                                 |
|  **3**   | **Gán màu & Kiểm tra** | Forward Checking | Thử gán màu từ list ["red", "green", "blue", "yellow"], kiểm tra không trùng với neighbors đã gán. |
|  **4**   | **Quay lui**           | Backtracking     | Nếu vùng không còn màu hợp lệ, quay lui: xóa gán, thử màu khác.                                    |
|  **5**   | **Tăng số màu**        | Optimization     | Nếu thất bại với k màu, thử k+1. Tìm số màu tối thiểu.                                             |
|  **6**   | **Kết thúc**           | Termination      | Thuật toán dừng khi gán hết vùng hoặc thử hết màu. Trả solution, min_colors, steps.                |

---

## 4. Luồng Dữ Liệu Giao Tiếp (API Data Contract)

Cấu trúc chuẩn của chuỗi JSON mà Backend (`app.py`) trả về cho Frontend (`script.js`):

**Thành công:**

```json
{
  "regions": {
    "0": {"neighbors": [1, 2], "points": [[x,y], ...], "color": "red"},
    "1": {"neighbors": [0, 2], "points": [[x,y], ...], "color": "blue"}
  },
  "steps": [
    {"type": "select", "node": 0, "message": "Chọn vùng 0"},
    {"type": "try", "node": 0, "color": "red", "message": "Thử red cho vùng 0"},
    {"type": "assign", "node": 0, "color": "red", "message": "Gán red cho vùng 0"},
    {"type": "backtrack", "node": 0, "message": "Quay lui vùng 0"},
    {"type": "success", "message": "Đã tìm thấy lời giải"}
  ],
  "min_colors": 3
}
```

**Lỗi (ảnh không hợp lệ):**

```json
{
  "error": "Ảnh phải có nền trắng và viền đen"
}
```

**Lỗi (không có file):**

```json
{
  "error": "Không có file"
}
```

**Lỗi (Không thể giải CSP - Status 400):**

```json
{
  "error": "Không thể tô màu ảnh này. Ảnh có thể quá phức tạp, bị nhiễu, hoặc không đáp ứng yêu cầu (nền trắng, viền đen rõ). Hãy thử PNG hoặc cải thiện chất lượng ảnh."
}
```

---

## 5. Xử Lý Lỗi (Error Handling)

- **Client-side:** Parse JSON trước, kiểm tra `!res.ok` hoặc `data.error` để hiển thị alert với thông báo lỗi.
- **Server-side:** Trả JSON với `error` field cho các trường hợp lỗi, không trả HTML.