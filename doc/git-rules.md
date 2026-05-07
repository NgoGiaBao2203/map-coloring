> **Author:** Ngô Gia Bảo
> **Created:** 05/05/2026  
> **Last Updated:** 07/05/2026   
> **Version:** 1.0.1

# Source Code Management Rules (Git Rules)

To ensure the project's source code remains clean, stable, and to avoid conflicts during teamwork, all members must read carefully and strictly follow the rules below.

## 1. Permissions and Branching Structure

*   **The `main` and `develop` branches are  protected  BRANCHES.**
*   **ABSOLUTELY DO NOT** push code directly to `main` and `develop`.
*   Only the **Leader** and **PM** have permission to operate (push/merge) on these 2 branches.
*   The team's shared working branch is **`develop`**. All new code, once completed, will be merged here. No one is allowed to work or merge code directly into the `main` and `develop` branches.

## 2. Branch Naming Convention

When receiving a new task (developing a new feature or fixing a bug), you must create a new branch from the `develop` branch using the following syntax:

*   **Syntax:** 
*   Create a new feature: `feature/v1/<branch-name-to-create>`
*   Fix a code bug: `bugfix/v1/<branch-name-to-fix>`
*   Document: `document/v1/<branch-name-to-doc>`
*   **Examples:** 
    *   `feature/v1/map-ui`
    *   `document/v1/run-project`
    *   `bugfix/v1/display-issue`

*(Note: Branch names must be lowercase, without accents, and words separated by hyphens `-`).*

## 3. Pre-Push Checklist

Before running the `git push` command, you **must** review your own code based on these 4 criteria:

1.  **Syntax Error:** Ensure the code has no red errors, and the program builds and runs successfully on your local machine.
2.  **Comment Out (Dead code):** Remove all draft code and old code that is commented out (`//` or `/* */`) to keep the files clean.
3.  **Naming Convention:** Ensure variables and functions are named properly and have clear meanings.
4.  **Comment Code:** Add brief explanatory comments in complex logic sections or important functions so other members can understand.

## 4. Commit Convention

*   **ENGLISH IS MANDATORY** for all commit messages.
*   Write concisely, going straight to the point of what you just did. 
*   **Examples:** `"add map rendering function"` or `"fix color overlap issue"`.

## 5. Code Submission Process (Pull Request & Merge)

Once you have finished the code on your personal `feature` or `bugfix` branch, please follow these steps:

1.  Push your `feature/v1/...`, etc. branch to GitHub.
2.  Create a **Pull Request (PR)** pointing from your branch to the **`develop`** branch.
V3.  **ASSIGN A REVIEWER:** You must tag/assign the **Leader** or **PM** to review your code.
4.  The Leader/PM will review the code. If the code passes, the Leader/PM will directly **Merge** your branch into `develop`. (If the code needs changes, the Leader will leave comments requesting modifications).

---
---

# Nội Quy Quản Lý Mã Nguồn (Git Rules)

Để đảm bảo source code của dự án luôn sạch sẽ, ổn định và tránh conflict khi làm việc nhóm, mọi thành viên vui lòng đọc kỹ và tuân thủ các quy tắc dưới đây.

## 1. Phân Quyền Và Cấu Trúc Nhánh (Branching)

*   **Nhánh `main` và `develop` là nhánh ĐƯỢC BẢO VỆ (Protected Branches).**
*   **TUYỆT ĐỐI KHÔNG** push code trực tiếp vào `main` và `develop`.
*   Chỉ có **Leader** và **PM** mới có quyền thao tác (push/merge) trên 2 nhánh này.
*   Nhánh làm việc chung của team là **`develop`**. Mọi code mới sau khi hoàn thiện sẽ được gộp vào đây. Không ai được phép làm việc hay merge code trực tiếp vào nhánh `main` và `develop`.

## 2. Quy Tắc Tạo Nhánh (Branch Naming)

Khi nhận task mới (làm tính năng mới hoặc sửa lỗi), bắt buộc phải tạo nhánh mới từ nhánh `develop` với cú pháp sau:

*   **Cú pháp:**  
*   Tạo tính năng mới `feature/v1/<tên-nhánh-cần-tạo>`
*   Sửa lỗi code `bugfix/v1/<tên-nhánh-cần-fix>`
*   Tài liệu: `document/v1/<tên-nhánh-cần-tài-liệu>`
*   **Ví dụ:** 
    *   `feature/v1/map-ui`
    *   `document/v1/run-project`
    *   `bugfix/v1/display-issue`

*(Lưu ý: Tên nhánh viết thường, không dấu, các từ cách nhau bằng dấu gạch ngang `-`).*

## 3. Checklist Trước Khi Push Code Lên Git

Trước khi gõ lệnh `git push`, bạn **bắt buộc** phải tự kiểm tra lại code của mình qua 4 tiêu chí sau:

1.  **Syntax Error (Lỗi cú pháp):** Đảm bảo code không báo lỗi đỏ, chương trình build và chạy thử thành công trên máy cá nhân.
2.  **Comment Out (Code rác):** Xóa toàn bộ các đoạn code nháp, code cũ bị `//` hoặc `/* */` (comment out) để file code được gọn gàng.
3.  **Naming Convention (Chuẩn đặt tên):** Đảm bảo tên biến, tên hàm đã được đặt đúng chuẩn, có ý nghĩa rõ ràng.
4.  **Comment Code:** Thêm comment giải thích ngắn gọn ở những đoạn logic phức tạp hoặc các hàm quan trọng để các thành viên khác đọc hiểu được.

## 4. Quy Tắc Viết Commit (Commit Convention)

*   **BẮT BUỘC sử dụng TIẾNG ANH** cho tất cả các thông điệp commit (Commit message).
*   Nên viết ngắn gọn, đi thẳng vào vấn đề vừa làm. 
*   **Ví dụ:** `"add map rendering function"` hoặc `"fix color overlap issue"`.

## 5. Quy Trình Nộp Code (Pull Request & Merge)

Khi đã hoàn thành code trên nhánh `feature` hoặc `bugfix` cá nhân, hãy thực hiện theo các bước sau:

1.  Push nhánh `feature/v1/...`,... của bạn lên GitHub.
2.  Tạo một **Pull Request (PR)** hướng từ nhánh của bạn vào nhánh **`develop`**.
3.  **ASSIGN A REVIEWER:** Bắt buộc phải tag/assign (chỉ định) **Leader** hoặc **PM** vào để review code.
4.  Leader/PM sẽ kiểm tra code. Nếu code đạt chuẩn, Leader/PM sẽ trực tiếp thực hiện lệnh **Merge** nhánh của bạn vào `develop`. (Nếu code chưa đạt, Leader sẽ comment yêu cầu sửa lại).