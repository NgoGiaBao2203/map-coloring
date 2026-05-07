> **Author:** Đặng Lê Thùy Dung
> **Created:** 05/05/2026  
> **Last Updated:** 05/05/2026   
> **Version:** 1.0.0

# Mô hình CSP (Constraint Satisfaction Problem)

---

## 1. Giới thiệu

Bài toán tô màu bản đồ có thể được mô hình hóa dưới dạng bài toán thỏa mãn ràng buộc (Constraint Satisfaction Problem - CSP). Đây là một mô hình phổ biến trong trí tuệ nhân tạo dùng để giải các bài toán có nhiều điều kiện ràng buộc.

---

## 2. Khái niệm CSP

Một bài toán CSP bao gồm 3 thành phần chính:

- **Biến (Variables):** các đối tượng cần gán giá trị  
- **Miền giá trị (Domains):** tập các giá trị có thể gán cho biến  
- **Ràng buộc (Constraints):** các điều kiện mà các biến phải thỏa mãn  

---

## 3. Áp dụng vào bài toán tô màu bản đồ

### 3.1 Biến (Variables)

Mỗi vùng trên bản đồ được xem là một biến.

Ví dụ:
- A, B, C, D,...

---

### 3.2 Miền giá trị (Domains)

Mỗi biến có thể nhận một trong các màu:

- {Đỏ, Xanh, Vàng, Cam,...}

---

### 3.3 Ràng buộc (Constraints)

Các vùng kề nhau không được có cùng màu.

Ví dụ:

A ≠ B  
B ≠ C  
C ≠ D  

---

## 4. Mục tiêu bài toán

Tìm cách gán màu cho tất cả các vùng sao cho:

- Thỏa mãn tất cả các ràng buộc  
- Không có hai vùng kề nhau cùng màu  

---

## 5. Biểu diễn bằng đồ thị

Bài toán có thể được biểu diễn dưới dạng đồ thị:

- Mỗi vùng là một đỉnh (node)  
- Mỗi cạnh (edge) biểu diễn mối quan hệ kề nhau  

Khi đó, bài toán trở thành bài toán tô màu đồ thị (Graph Coloring).

---

## 6. Độ khó của bài toán

- Số lượng khả năng tăng rất nhanh theo số vùng  
- Nếu không tối ưu, thuật toán sẽ chạy chậm  

Vì vậy cần kết hợp với:
- Backtracking  
- Heuristic  

---

## 7. Kết luận

Mô hình CSP giúp biểu diễn bài toán một cách rõ ràng và có hệ thống. Đây là cơ sở để áp dụng các thuật toán như Backtracking và Heuristic nhằm tìm lời giải hiệu quả.

---