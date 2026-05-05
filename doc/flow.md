# LUỒNG HOẠT ĐỘNG CỦA HỆ THỐNG (SYSTEM FLOW)

Dự án Map Coloring áp dụng kiến trúc Client - Server cơ bản:
- **Client (Frontend):** `index.html`, `style.css`, `script.js` (Xử lý giao diện và hiệu ứng).
- **Server (Backend):** `app.py` (Xử lý API và chạy thuật toán AI).

---

## 1. Luồng Tương Tác Tổng Thể (User Flow)

| Bước  | Quá trình                  |    Nơi xử lý    | Chi tiết hoạt động                                                                                                                    |
| :---: | :------------------------- | :-------------: | :------------------------------------------------------------------------------------------------------------------------------------ |
| **1** | **Khởi tạo giao diện**     | Client / Server | Người dùng truy cập web. Flask (`app.py`) render file `index.html`. Bản đồ SVG hiện ra với màu trắng/xám mặc định.                    |
| **2** | **Gửi yêu cầu (Trigger)**  |   Client (JS)   | Người dùng bấm nút **"Tô màu bản đồ"**. `script.js` bắt sự kiện click và gọi `fetch()` gửi HTTP Request (GET) tới API (`/api/solve`). |
| **3** | **Xử lý thuật toán**       |   Server (AI)   | Flask nhận request, kích hoạt module Đồ thị (Graph) và chạy thuật toán **Backtracking + Heuristic** để tìm đáp án.                    |
| **4** | **Trả kết quả (Response)** |  Server (API)   | Sau khi tìm được tập màu hợp lệ, `app.py` đóng gói kết quả thành chuỗi JSON và gửi trả về cho Frontend.                               |
| **5** | **Hiển thị (Animation)**   |   Client (JS)   | `script.js` nhận JSON, dùng vòng lặp và `setTimeout()` để đổi màu (`fill`) từng thẻ `<path>` trên SVG theo thứ tự, tạo animation.     |

---

## 2. Luồng Chạy Core AI (Backtracking + Heuristic Flow)

Chi tiết quy trình xử lý bên trong **Bước 3** của hệ thống (Phần logic cốt lõi do AI đảm nhận):

| Trình tự | Giai đoạn xử lý        | Kỹ thuật áp dụng | Mô tả chi tiết                                                                                                                                                        |
| :------: | :--------------------- | :--------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  **1**   | **Khởi tạo Đồ thị**    |   Graph Build    | Nạp danh sách các khu vực và các cạnh kề (ràng buộc). Đưa vào cấu trúc dữ liệu đồ thị (Danh sách kề hoặc Ma trận kề).                                                 |
|  **2**   | **Chọn biến**          |    Heuristic     | Dùng Heuristic chọn vùng tiếp theo cần tô:<br>- **MRV:** Ưu tiên vùng còn ít lựa chọn màu nhất.<br>- **Degree:** Ưu tiên vùng có nhiều hàng xóm nhất.                 |
|  **3**   | **Gán màu & Kiểm tra** | Forward Checking | Thử gán màu cho vùng vừa chọn và kiểm tra trùng lặp:<br>- **Hợp lệ:** Lưu trạng thái, đệ quy sang vùng tiếp theo.<br>- **Trùng màu:** Bỏ qua, thử màu khác trong tập. |
|  **4**   | **Quay lui**           |   Backtracking   | Nếu một vùng không còn màu nào hợp lệ (mọi màu đều trùng), hệ thống **quay lui** về vùng trước đó, xóa màu cũ và thử màu mới.                                         |
|  **5**   | **Kết thúc**           |   Termination    | Thuật toán dừng khi TẤT CẢ các vùng đã được tô màu hợp lệ. Trả danh sách kết quả ra cho API.                                                                          |

---

## 3. Luồng Dữ Liệu Giao Tiếp (API Data Contract)

Cấu trúc chuẩn của chuỗi JSON mà Backend (`app.py`) sẽ trả về cho Frontend (`script.js`) để xử lý hiệu ứng:

```json
{
  "status": "success",
  "total_regions": 10,
  "colors_used": 4,
  "steps": [
    {"id": "VN", "color": "#FF0000"},
    {"id": "LA", "color": "#0000FF"},
    {"id": "KH", "color": "#00FF00"}
  ]
}