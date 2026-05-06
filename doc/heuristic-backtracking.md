# Thuật toán Backtracking và Heuristic

---

## 1. Giới thiệu

Trong bài toán tô màu bản đồ, mục tiêu là gán màu cho các vùng sao cho không có hai vùng kề nhau có cùng màu. Đây là một bài toán điển hình có thể giải bằng thuật toán Backtracking kết hợp với Heuristic để tăng hiệu quả.

---

## 2. Thuật toán Backtracking

### 2.1 Khái niệm

Backtracking (quay lui) là phương pháp tìm kiếm lời giải bằng cách thử tất cả các khả năng. Khi gặp lựa chọn không hợp lệ, thuật toán sẽ quay lại bước trước đó và thử phương án khác.

---

### 2.2 Cách hoạt động

Thuật toán thực hiện theo các bước:

1. Chọn một vùng chưa được tô màu  
2. Thử gán một màu cho vùng đó  
3. Kiểm tra ràng buộc với các vùng kề  
4. Nếu hợp lệ thì tiếp tục với vùng tiếp theo  
5. Nếu không hợp lệ thì quay lui và thử màu khác  

---

### 2.3 Ví dụ minh họa

Giả sử có 3 vùng A, B, C với hai màu (Đỏ, Xanh):

- A → Đỏ  
- B → Xanh  
- C → không thể chọn màu hợp lệ → quay lại B và thử màu khác  

---

### 2.4 Pseudocode

```pseudo
function backtrack(assignment):
    if tất cả vùng đã tô:
        return assignment

    chọn vùng chưa tô

    for mỗi màu:
        if hợp lệ:
            gán màu
            nếu backtrack thành công:
                return kết quả
            bỏ gán (quay lui)

    return thất bại
```
### 2.5 Ưu điểm và nhược điểm

**Ưu điểm:**
- Đảm bảo tìm được lời giải nếu tồn tại  

**Nhược điểm:**
- Tốn thời gian khi số lượng vùng lớn  

---

## 3. Heuristic

### 3.1 Khái niệm

Heuristic là phương pháp giúp cải thiện hiệu suất bằng cách đưa ra lựa chọn thông minh hơn thay vì thử ngẫu nhiên.

---

### 3.2 Áp dụng

- Chọn vùng có nhiều ràng buộc nhất trước  
- Chọn màu ít gây xung đột nhất  

---

### 3.3 Ví dụ

Thay vì chọn ngẫu nhiên:

- Chọn vùng có nhiều hàng xóm trước giúp phát hiện xung đột sớm  
- Giảm số lần quay lui  

---

### 3.4 Lợi ích

- Giảm số bước tìm kiếm  
- Tăng tốc độ xử lý  
- Hiệu quả hơn Backtracking thuần  

---

## 4. Kết hợp Backtracking và Heuristic

- Backtracking đảm bảo tìm được lời giải  
- Heuristic giúp tìm lời giải nhanh hơn  

Đây là cách tiếp cận hiệu quả cho bài toán tô màu bản đồ.

---

## 5. Kết luận

Backtracking là nền tảng để giải bài toán tô màu bản đồ. Việc kết hợp với Heuristic giúp tối ưu hiệu suất, giảm thời gian xử lý và nâng cao hiệu quả tìm kiếm lời giải.