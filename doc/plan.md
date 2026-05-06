# KẾ HOẠCH VÀ PHÂN CÔNG ĐỒ ÁN: MAP COLORING

## 1. Thông Tin Chung
*   **Đề tài 23:** Giải bài toán tô màu bản đồ (Map Coloring) bằng thuật toán Tìm kiếm Quay lui (Backtracking) kết hợp Heuristic.
*   **Mục tiêu:** Tô màu bản đồ sao cho các khu vực kề nhau không trùng màu, sử dụng số lượng màu tối thiểu.
*   **Thời gian thực hiện:** 05/05/2026 - 09/05/2026 (Chạy nước rút 5 ngày)
*   **Nhóm thực hiện:** 5 thành viên.

---

## 2. Bảng Phân Công Công Việc Chi Tiết

|  STT  | Họ và Tên             |  MSSV  | Vai trò           | Chi tiết công việc (Tasks)                                                                                                                                                                                                        |
| :---: | :-------------------- | :----: | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Ngô Gia Bảo**       | 239922 | Leader / Backend  | - Khởi tạo source base (Flask, Git flow).<br>- Tích hợp Heuristic (ưu tiên khu vực nhiều ràng buộc) vào core AI.<br>- Viết API Endpoint (`app.py`) để giao tiếp với Frontend.<br>- Code Review và Merge code vào nhánh `develop`. |
| **2** | **Hồ Văn Tài**        | 233015 | Dev AI / Backend  | - Thiết kế cấu trúc dữ liệu đồ thị (Graph) cho bản đồ.<br>- Lập trình core AI: Áp dụng thuật toán Backtracking.<br>- Hỗ trợ test luồng dữ liệu thuật toán.                                                                        |
| **3** | **Dương Trí Thành**   | 233012 | Dev JS / PPT      | - Xử lý logic file `script.js`: Fetch API từ Python.<br>- Lập trình hiệu ứng (Animation) tô màu từng bước lên bản đồ.<br>- Thiết kế Slide thuyết trình (PPT).                                                                     |
| **4** | **Đặng Lê Thuỳ Dung** | 232836 | Dev UI / Document | - Phối hợp code Frontend: giao diện khung `index.html` và định dạng `style.css`.<br>- Viết tài liệu thuật toán.                                                                                                                   |
| **5** | **Lê Thị Như Ý**      | 232948 | Dev UI / Data     | - Tìm kiếm, xử lý file bản đồ SVG, gắn ID cho các vùng.<br>- Phối hợp code Frontend: hỗ trợ `index.html` và `style.css`.<br>- Viết tài liệu hướng dẫn chạy dự án (`README.md`).                                                   |

---

## 3. Lộ Trình Thực Hiện Từng Ngày (Chạy Sprint 5 Ngày)

*   **Ngày 1 (05/05) - Khởi tạo & Dữ liệu:**
    *   Bảo: Lên khung code base Flask, đẩy lên Git, tạo các nhánh.
    *   Tài: Xác định cách lưu trữ Graph (ma trận kề hoặc danh sách kề).
    *   Ý & Dung: Chốt file bản đồ SVG, dựng xong layout HTML/CSS cơ bản. Chốt danh sách ID các vùng.
*   **Ngày 2 (06/05) - Lập trình Core AI:**
    *   Tài: Code xong thuật toán Backtracking thuần, test ra kết quả trên terminal.
    *   Bảo: Tham gia bọc thêm thuật toán Heuristic vào code của Tài để tối ưu.
    *   Thành: Bắt đầu viết JS với dữ liệu JSON, làm hiệu ứng animation.
*   **Ngày 3 (07/05) - Kết nối hệ thống:**
    *   Bảo: Viết xong API Endpoint trong `app.py` trả về luồng JSON.
    *   Thành: Xóa dữ liệu giả, gọi API thật của Bảo để hiển thị lên bản đồ do Ý/Dung làm.
    *   Team Frontend (Dung, Ý): Chỉnh trang lại CSS cho mượt và đẹp.
*   **Ngày 4 (08/05) - Fix Bug & Tài liệu:**
    *   Cả nhóm: Chạy thử toàn bộ luồng (Bấm nút -> Gọi API -> Trả kết quả -> Tô màu). Fix các lỗi phát sinh.
    *   Dung: Bắt đầu viết các file Document trong thư mục `doc/`.
    *   Ý: Viết `README.md`.
*   **Ngày 5 (09/05) - Hoàn thành**
    *   Thành: Hoàn thiện Slide thuyết trình (PPT).
    *   Cả nhóm: Kiểm tra lại toàn bộ code, test lại.
*   **Ngày 6 (12/05) - Chính thức hoàn thành - Báo cáo**
    *   Kiểm tra lần cuối trước khi báo cáo.
    *   Bảo: Kiểm tra lại toàn bộ code, clean code, merge tất cả lên nhánh `develop`. Hoàn đề tài!
## 4. Ghi Chú
*   Các thành viên tuân thủ đúng nội quy Git (`git_rules.md`) khi push/pull code.
*   Nếu gặp khó khăn/bug quá 1 ngày chưa fix được, lập tức báo cáo cho Leader để được support, tránh làm trễ tiến độ chung.
