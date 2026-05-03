# 🎨 Giải Bài Toán Tô Màu Bản Đồ (Map Coloring CSP)

**Môn học:** Trí tuệ Nhân tạo (Artificial Intelligence)  
**Đề tài 23:** Giải bài toán tô màu bản đồ bằng thuật toán Tìm kiếm Quay lui (Backtracking) kết hợp Heuristic.  
**Ngôn ngữ & Công nghệ:** Python (Flask), HTML, CSS, JavaScript.  

---

## 📋 Mục Lục
1. [1. Giới Thiệu](#1--giới-thiệu)
2. [2. Cấu Trúc Thư Mục](#2--cấu-trúc-thư-mục)
---

## 1. 🎯 Giới Thiệu
Dự án là một ứng dụng Web trực quan hóa quá trình giải **Bài toán tô màu bản đồ (Map Coloring Problem)** - một dạng kinh điển của Bài toán thỏa mãn ràng buộc (CSP). 

Yêu cầu bài toán: Tô màu các vùng miền trên bản đồ (được định nghĩa trước) bằng số lượng màu tối thiểu (3 màu) sao cho **không có 2 vùng nào kề nhau lại có cùng một màu**.

**Tính năng nổi bật:**
- Backend xử lý thuật toán thuần túy bằng **Python**.
- Áp dụng thuật toán **Backtracking** (Tìm kiếm quay lui).
- Kết hợp **Degree Heuristic** để tối ưu hóa việc chọn biến.
- Frontend mô phỏng (Animation) từng bước thử màu, gán màu và quay lui một cách trực quan trên bản đồ SVG.

---

## 2. 🏗 Cấu Trúc Thư Mục

Dự án được triển khai theo cấu trúc chuẩn của một ứng dụng Web Python Flask:

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
└── README.md               # File tài liệu dự án (bạn đang đọc)