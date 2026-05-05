**Author:** Gia Bao  
**Created:** 04/05/2026  
**Last Updated:** 04/05/2026  
**Version:** V1.0

# Đề tài 23: Giải bài toán tô màu bản đồ (Map Coloring) bằng thuật toán Tìm kiếm Quay lui (Backtracking) kết hợp Heuristic

* **Yêu cầu:** Tô màu một bản đồ sao cho các khu vực kề nhau có màu khác nhau, sử dụng số lượng màu tối thiểu.
* **Tập trung vào:**
  * Mô hình hóa bài toán thành bài toán thỏa mãn ràng buộc (CSP).
  * Sử dụng Heuristic để chọn biến tiếp theo (v.d.: ưu tiên khu vực có nhiều ràng buộc nhất).
  * Cài đặt thuật toán Backtracking để tìm ra lời giải hợp lệ.

---

### Dung: Cơ sở lý thuyết và Mô hình hóa (CSP)
**Trọng tâm:** Chuyển từ bản đồ thực tế sang ngôn ngữ toán học/lập trình.

* **Khái niệm cơ bản:** Định nghĩa bài toán Tô màu bản đồ và lý thuyết Đồ thị (nút là khu vực, cạnh là đường biên giới).
* **Mô hình hóa bài toán thỏa mãn ràng buộc (CSP):**
  * **Variables (X):** Danh sách các khu vực cần tô màu.
  * **Domains (D):** Tập hợp các màu sắc khả dụng (ví dụ: {Đỏ, Xanh lá, Xanh dương, Vàng}).
  * **Constraints (C):** Các ràng buộc cứng (hai khu vực kề nhau/có chung cạnh thì không được cùng màu).
* **Số sắc số (Chromatic Number):** Giải thích ngắn gọn về định lý 4 màu và mục tiêu tìm số lượng màu tối thiểu.

### Ý: Thuật toán và Chiến lược Heuristic
**Trọng tâm:** Cách máy tính "tư duy" để tìm lời giải nhanh hơn.

* **Thuật toán Backtracking (Quay lui):** Giải thích quy trình thử - sai, nếu gặp ngõ cụt (vi phạm ràng buộc) thì quay lại bước trước để chọn màu khác.
* **Các kỹ thuật Heuristic để tăng tốc:**
  * **Minimum Remaining Values (MRV):** Ưu tiên chọn khu vực còn ít lựa chọn màu nhất (khu vực "nguy hiểm" nhất).
  * **Degree Heuristic:** Ưu tiên chọn khu vực có nhiều láng giềng chưa tô màu nhất (để sớm phát hiện lỗi).
  * **Least Constraining Value (LCV):** Khi chọn màu, chọn màu nào ít gây ảnh hưởng đến các lựa chọn của các khu vực láng giềng nhất.
  
### 📌 Tài, Bảo, Thành: Cài đặt thuật toán và Đánh giá
**Trọng tâm:** Lập trình giải pháp và chứng minh hiệu quả của thuật toán.

* **Cài đặt thuật toán Backtracking:** Lập trình quy trình quay lui cốt lõi để giải quyết bài toán trên danh sách các biến đã được mô hình hóa.
* **Tích hợp các Heuristic:** Đưa các kỹ thuật MRV, Degree Heuristic và LCV vào bộ chọn biến/giá trị trong lúc chạy thuật toán.
* **Thử nghiệm và Demo:** Chạy chương trình với các bộ dữ liệu bản đồ mẫu (ví dụ: bản đồ Úc, bản đồ Việt Nam). Đánh giá và so sánh thời gian, số bước lặp giữa Backtracking thuần túy và Backtracking kết hợp Heuristic.

**Phân Tích Flow Chạy**

* **Bước 1: Khởi tạo và Tương tác (Frontend)**
  * **Mô tả:** Người dùng truy cập trang giao diện (`index.html`), lựa chọn cấu hình và nhấn nút bắt đầu giải quyết bài toán[cite: 3].
  * **Ánh xạ code:** File `index.html` cung cấp giao diện trực quan với bản đồ SVG chứa các `polygon` đại diện cho các khu vực[cite: 3]. Nút tương tác được gắn sự kiện `onclick="startSolve()"`[cite: 3].

* **Bước 2: Gửi yêu cầu giải quyết (Frontend -> Backend)**
  * **Mô tả:** File `script.js` bắt sự kiện click, lấy thông tin cấu hình và gửi một HTTP Request mang theo dữ liệu về server[cite: 4].
  * **Ánh xạ code:** Hàm `startSolve()` trong `script.js` sử dụng `fetch("/solve")` để gửi một GET request tới route `/solve` của backend Python[cite: 4].

* **Bước 3: Xử lý logic thuật toán (Backend - `app.py`)**
  * **Mô tả:** Server khởi tạo mô hình CSP, chạy Backtracking kết hợp Heuristic, và ghi nhận lại toàn bộ "lịch sử" các bước[cite: 1].
  * **Ánh xạ code:**
    * **Khởi tạo CSP:** Hàm `solve_map()` tiếp nhận yêu cầu, định nghĩa các biến `regions`, `colors`, `neighbors` và khởi tạo object `MapColoringCSP`[cite: 1].
    * **Tích hợp Heuristic:** Áp dụng **Degree Heuristic** trong hàm `select_unassigned_variable` bằng cách ưu tiên khu vực có nhiều láng giềng nhất thông qua đoạn code: `unassigned.sort(key=lambda var: len(self.neighbors.get(var, [])), reverse=True)`[cite: 1].
    * **Chạy Quay lui & Ghi Log:** Xuyên suốt hàm đệ quy `backtrack()`, mỗi trạng thái thử màu (`try`), gán hợp lệ (`assign`), vi phạm (`invalid`), hay quay lui (`backtrack`) đều được lưu vào mảng `self.steps` dưới dạng dictionary[cite: 1].

* **Bước 4: Trả kết quả (Backend -> Frontend)**
  * **Mô tả:** Server đóng gói toàn bộ lịch sử các bước giải thành định dạng JSON rồi gửi về lại cho trình duyệt[cite: 1].
  * **Ánh xạ code:** Cuối quá trình xử lý, `app.py` trả về dữ liệu cho trình duyệt thông qua lệnh `return jsonify({"success": True, "steps": steps})`[cite: 1].

* **Bước 5: Trình diễn trực quan (Frontend)**
  * **Mô tả:** `script.js` nhận dữ liệu JSON, phân tích và cập nhật DOM theo từng bước với độ trễ để tạo Animation[cite: 4].
  * **Ánh xạ code:** Biến `data` nhận toàn bộ cục JSON[cite: 4]. Vòng lặp `for (let step of data.steps)` sẽ duyệt qua từng bước giải[cite: 4]. Màu của khu vực trên bản đồ SVG được thay đổi liên tục bằng `document.getElementById(step.region).style.fill = step.color`[cite: 4]. Để người xem thấy rõ cách máy tính "tư duy", thuật toán sử dụng hàm `await sleep(delay);` (với độ trễ 350ms) để tạm dừng giữa các thao tác[cite: 4].

Dự án được triển khai theo cấu trúc chuẩn của một ứng dụng Web Python Flask:

**Cấu Trúc Thư Mục**
```text
map-coloring/
│
├── static/                 # Chứa các file tĩnh (Frontend)
│   ├── script.js           # Xử lý gọi API sang Python và tạo Animation
│   └── style.css           # Định dạng giao diện Web (Layout 2 cột)
│
├── templates/              # Chứa các file HTML (Flask bắt buộc để ở đây)
│   └── index.html          # Giao diện chính chứa bản đồ SVG
│
├── app.py                  # File chạy chính (Backend Server & AI Logic)
└── README.md