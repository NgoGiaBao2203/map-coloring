# 🎨 Bài Toán Tô Màu Bản Đồ - Map Coloring CSP Solver

**Tác giả:** Full-stack Developer + AI Expert  
**Ngôn Ngữ:** Python (Backend) + JavaScript (Frontend)  
**Ngày:** 2026

---

## 📋 Mục Lục

1. [Giới Thiệu](#giới-thiệu)
2. [Kiến Trúc Dự Án](#kiến-trúc-dự-án)
3. [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
4. [Hướng Dẫn Cài Đặt](#hướng-dẫn-cài-đặt)
5. [Hướng Dẫn Chạy](#hướng-dẫn-chạy)
6. [Cách Sử Dụng](#cách-sử-dụng)
7. [API Documentation](#api-documentation)
8. [Giải Thích Thuật Toán](#giải-thích-thuật-toán)
9. [Cấu Trúc Code](#cấu-trúc-code)

---

## 🎯 Giới Thiệu

Đây là một ứng dụng web hoàn chỉnh giải quyết **Bài Toán Tô Màu Bản Đồ (Map Coloring Problem)** - một vấn đề kinh điển trong Trí Tuệ Nhân Tạo và Khoa Học Máy Tính.

### Bài Toán Là Gì?

**Map Coloring Problem** là một bài toán Constraint Satisfaction Problem (CSP) với các yêu cầu:
- Cho một bản đồ (đồ thị) với các vùng (đỉnh) và các ranh giới (cạnh)
- Tô màu cho mỗi vùng sao cho hai vùng kề nhau có màu khác nhau
- Mục tiêu: Tìm số lượng màu tối thiểu cần để tô bản đồ

### Ví Dụ Thực Tế

Bản đồ Úc:
```
┌─────────────┐
│     WA      │
├─────────────┤
│  NT │ QLD   │
├─────────────┤
│ SA  │NSW│V  │
└─────────────┘
```

- **Đỉnh:** WA, NT, QLD, NSW, V, SA, T (7 bang/lãnh thổ)
- **Cạnh:** Các cặp vùng kề nhau
- **Giải Pháp:** Cần tối thiểu 3 màu để tô bản đồ Úc

---

## 🏗️ Kiến Trúc Dự Án

### 📁 Cấu Trúc Thư Mục

```
map-coloring/
│
├── 📂 backend/                    # Backend Python + Flask
│   ├── app.py                     # Flask Server + API Endpoints
│   ├── csp_solver.py             # AI Logic: Backtracking + Heuristics
│   ├── requirements.txt           # Dependencies
│   └── __pycache__/              # Cache Python
│
├── 📂 frontend/                   # Frontend HTML/CSS/JS
│   ├── index.html                # Giao diện chính
│   ├── 📂 css/
│   │   └── style.css             # Styling (Modern, Responsive)
│   ├── 📂 js/
│   │   └── app.js                # JavaScript: Logic + API calls + vis.js
│   └── 📂 data/
│       └── samples.json          # Dữ liệu mẫu (tùy chọn)
│
├── README.md                      # Hướng dẫn này
├── .gitignore                     # Git ignore rules
└── .git/                          # Git repository

```

### 🔧 Technology Stack

| Layer             | Technology    | Mục Đích                         |
| ----------------- | ------------- | -------------------------------- |
| **Backend**       | Python 3.8+   | AI logic, Server-side processing |
| **Web Framework** | Flask 2.3+    | REST API, CORS support           |
| **Frontend**      | HTML5/CSS3/JS | User Interface                   |
| **Visualization** | vis.js        | Vẽ biểu đồ interactively         |
| **API**           | RESTful JSON  | Backend-Frontend communication   |

---

## 💻 Yêu Cầu Hệ Thống

### Phần Cứng
- **CPU:** Intel/AMD (modern)
- **RAM:** Tối thiểu 2GB
- **Disk:** 100MB (không tính dữ liệu)

### Phần Mềm
- **Python:** 3.8 hoặc cao hơn
- **Node.js/npm:** (Tùy chọn, không bắt buộc)
- **Browser:** Chrome, Firefox, Edge, Safari (hỗ trợ ES6+)

---

## 🚀 Hướng Dẫn Cài Đặt

### Step 1: Clone Repository

```bash
cd C:\03_Workspace_Education\University_Documents\Trí\ tuệ\ nhân\ tạo\ -\ artificail\ intelligence\CodeAll
git clone <repository-url> map-coloring
cd map-coloring
```

### Step 2: Cài Đặt Python Dependencies

```bash
# Vào thư mục backend
cd backend

# Tạo Virtual Environment (Recommended)
python -m venv venv

# Kích hoạt Virtual Environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt
```

### Step 3: Kiểm Tra Cài Đặt

```bash
# Kiểm tra phiên bản Python
python --version

# Kiểm tra Flask đã cài chưa
pip list | grep flask
```

---

## 🎮 Hướng Dẫn Chạy

### Bước 1: Chạy Backend Server

```bash
# Từ thư mục backend (với venv kích hoạt)
python app.py
```

**Kết Quả:**
```
🚀 Khởi động Flask server...
📍 Server chạy tại http://localhost:5000
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Bước 2: Mở Frontend

```bash
# Cách 1: Mở trực tiếp file (không cần server)
cd frontend
# Nhấp đôi vào index.html
# Hoặc dùng browser: Ctrl+O chọn file

# Cách 2: Dùng Live Server (tốt hơn)
# Nếu có Node.js:
npx http-server frontend -p 8000
# Mở browser: http://localhost:8000
```

### Bước 3: Kiểm Tra Kết Nối

Mở browser Console (F12) và kiểm tra:
```javascript
// Trong Console:
fetch('http://localhost:5000/api/samples')
  .then(r => r.json())
  .then(d => console.log(d))
```

---

## 📖 Cách Sử Dụng

### Giao Diện Người Dùng

```
┌─────────────────────────────────────────────────────────────┐
│  🎨 Giải Bài Toán Tô Màu Bản Đồ                            │
│  Map Coloring Problem - CSP Solver                         │
└─────────────────────────────────────────────────────────────┘
│
├─ 📋 ĐIỀU KHIỂN (Trái)     │  📊 BIỂU ĐỒ (Phải)
│                            │
│  ⚙️ Chọn Dữ Liệu Mẫu:      │  [Biểu đồ vis.js]
│  └─ Bản đồ Úc             │
│  └─ Bản đồ Châu Âu        │  Hiển thị:
│  └─ Đồ thị Đơn Giản       │  - Các đỉnh (nodes)
│                            │  - Các cạnh (edges)
│  📝 Nhập Vertices:         │  - Màu sắc theo giải pháp
│  └─ A, B, C, D           │
│                            │
│  🔗 Nhập Edges:           │
│  └─ A-B, B-C, ...        │
│                            │
│  🎨 Số Màu:              │
│  └─ (để trống = auto)    │
│                            │
│  [🚀 Bắt Đầu] [🗑️ Xóa]   │
│                            │
│  ✅ Kết Quả:             │
│  └─ Số màu, backtrack... │
│
└────────────────────────────────────────────────────────────┘
```

### Các Bước Sử Dụng

#### **Cách 1: Dùng Dữ Liệu Mẫu (Nhanh nhất)**

1. Chọn "Bản đồ Úc" từ dropdown "Chọn Dữ Liệu Mẫu"
2. Dữ liệu sẽ tự điền vào form
3. Nhấp "🚀 Bắt Đầu Giải"
4. Xem kết quả:
   - Biểu đồ được vẽ với màu sắc
   - Thông tin: số màu, số lần backtrack
   - Gán màu chi tiết cho mỗi đỉnh

#### **Cách 2: Nhập Dữ Liệu Tùy Chỉnh**

1. **Nhập Vertices:**
   ```
   A, B, C, D
   ```
   Hoặc:
   ```
   WA, NT, QLD, NSW, V, SA
   ```

2. **Nhập Edges (Cạnh - quan hệ kề nhau):**
   ```
   A-B, B-C, C-D, D-A
   ```
   
   Hoặc:
   ```
   WA-NT, WA-SA, NT-SA, NT-QLD, ...
   ```

3. **Tùy chọn Số Màu:**
   - Để trống: Tìm tự động (khuyên dùng)
   - Nhập số: Dùng số màu cố định (VD: 3)

4. Nhấp "🚀 Bắt Đầu Giải"

5. Xem kết quả

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. **GET /api/samples** - Lấy Dữ Liệu Mẫu

**Request:**
```bash
GET http://localhost:5000/api/samples
```

**Response (Success):**
```json
{
  "success": true,
  "data": {
    "australia": {
      "name": "Bản đồ Úc",
      "vertices": ["WA", "NT", "QLD", "NSW", "V", "SA", "T"],
      "edges": [["WA", "NT"], ["WA", "SA"], ...]
    },
    "europe": {...},
    "simple": {...}
  }
}
```

---

#### 2. **POST /api/solve** - Giải Bài Toán

**Request:**
```bash
POST http://localhost:5000/api/solve
Content-Type: application/json

{
  "vertices": ["A", "B", "C", "D"],
  "edges": [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]],
  "num_colors": null
}
```

**Parameters:**
| Parameter    | Type                 | Required | Description                 |
| ------------ | -------------------- | -------- | --------------------------- |
| `vertices`   | Array<String>        | ✅        | Danh sách tên đỉnh          |
| `edges`      | Array<Array<String>> | ✅        | Danh sách cạnh (cặp đỉnh)   |
| `num_colors` | Integer/null         | ❌        | Số màu (null = tìm tự động) |

**Response (Success):**
```json
{
  "success": true,
  "solution": {
    "A": "color_0",
    "B": "color_1",
    "C": "color_0",
    "D": "color_1"
  },
  "num_colors": 2,
  "backtrack_count": 3,
  "message": "Tìm được giải pháp với 2 màu"
}
```

**Response (Failure):**
```json
{
  "success": false,
  "error": "Danh sách vertices không thể rỗng"
}
```

---

#### 3. **POST /api/validate** - Kiểm Tra Đồ Thị

**Request:**
```bash
POST http://localhost:5000/api/validate
Content-Type: application/json

{
  "vertices": ["A", "B", "C"],
  "edges": [["A", "B"], ["B", "C"]]
}
```

**Response:**
```json
{
  "success": true,
  "valid": true,
  "errors": []
}
```

---

#### 4. **GET /** - Thông Tin API

**Request:**
```bash
GET http://localhost:5000/
```

**Response:**
```json
{
  "name": "Map Coloring CSP Solver API",
  "version": "1.0",
  "endpoints": {...}
}
```

---

## 🤖 Giải Thích Thuật Toán

### Bài Toán CSP (Constraint Satisfaction Problem)

```
Variables: Các đỉnh (regions)
Domains: Các màu có sẵn (color_0, color_1, ...)
Constraints: Các đỉnh kề phải khác màu
```

### Thuật Toán Backtracking

#### Pseudocode:

```python
def backtrack(assignment, domains):
    # Nếu tất cả biến được gán -> Tìm được giải pháp
    if all assigned:
        return True
    
    # Chọn biến chưa gán (dùng Heuristic)
    var = select_unassigned_variable()
    
    # Thử từng giá trị từ domain
    for value in domains[var]:
        if is_consistent(var, value):  # Kiểm tra ràng buộc
            assignment[var] = value
            
            # Cập nhật domain (Constraint Propagation)
            old_domains = copy(domains)
            update_domains(var, value, domains)
            
            # Đệ quy
            if backtrack(assignment, domains):
                return True
            
            # Backtrack
            assignment[var] = None
            domains = old_domains
    
    return False
```

### Heuristics (Chiến Lược Tối Ưu)

#### 1️⃣ **MRV (Minimum Remaining Values)**

Chọn biến có ít giá trị còn lại nhất:

```
Variables: A (3 colors), B (1 color), C (4 colors)
Chọn: B (vì chỉ còn 1 color)
```

**Lợi Ích:** Phát hiện sớm các xung đột, giảm độ sâu tìm kiếm

#### 2️⃣ **Degree Heuristic**

Nếu hòa về MRV, chọn biến kề với nhiều biến chưa gán:

```
Nodes: A (kề 3 node), B (kề 1 node)
Cùng MRV? Chọn A
```

**Lợi Ích:** Giới hạn domain của các biến phía sau

#### 3️⃣ **Constraint Propagation**

Khi gán value cho var, xóa value khỏi domain của các đỉnh kề:

```
Gán: A = red
Cập nhật: Domain của (B, C) xóa "red"
```

---

### Flow Giải Toán

```
┌─ Input: Vertices, Edges
│
├─ 1. Xây dựng Adjacency List (danh sách kề)
│
├─ 2. Khởi tạo Domains (tất cả màu khả dụng)
│
├─ 3. Lặp từ num_colors = 1, 2, 3, ...
│  │
│  ├─ Gọi Backtracking(domains):
│  │  │
│  │  ├─ Chọn var chưa gán (MRV + Degree)
│  │  │
│  │  ├─ Thử từng color từ domain[var]:
│  │  │  │
│  │  │  ├─ Kiểm tra: color nhất quán?
│  │  │  │
│  │  │  ├─ Nếu YES: Gán + Cập nhật domain + Đệ quy
│  │  │  │
│  │  │  ├─ Nếu Đệ quy thành công -> Return True
│  │  │  │
│  │  │  ├─ Nếu Đệ quy thất bại -> Backtrack
│  │  │
│  │  ├─ Return False (không tìm được)
│  │
│  ├─ Nếu tìm được -> Return solution
│
├─ 4. Return kết quả (solution + num_colors + backtrack_count)
│
└─ Output: JSON với gán màu cho mỗi đỉnh
```

---

## 📝 Cấu Trúc Code

### Backend: `csp_solver.py`

```python
class MapColoringSolver:
    """
    Lớp chính giải CSP
    
    Methods:
    - solve(num_colors): API chính
    - _solve_with_k_colors(k): Giải với k màu
    - _backtrack(domains): Thuật toán Backtracking
    - _select_unassigned_variable(domains): Chọn biến (MRV + Degree)
    - _is_consistent(var, value): Kiểm tra ràng buộc
    - _update_domains(var, value, domains): Constraint Propagation
    """
    
    def __init__(self, vertices, edges):
        # Khởi tạo
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = self._build_adjacency_list()
        self.assignment = {v: None for v in vertices}
    
    def solve(self, num_colors=None):
        # API chính: tìm tự động hoặc dùng num_colors
        pass
    
    # ... (các method khác)
```

### Backend: `app.py`

```python
@app.route('/api/solve', methods=['POST'])
def solve_map_coloring():
    """
    API Endpoint chính
    - Lấy vertices, edges từ request JSON
    - Tạo MapColoringSolver instance
    - Gọi solve()
    - Trả về JSON response
    """
    pass

@app.route('/api/samples', methods=['GET'])
def get_samples():
    """Trả về dữ liệu mẫu"""
    pass

@app.route('/api/validate', methods=['POST'])
def validate_graph():
    """Kiểm tra tính hợp lệ của đồ thị"""
    pass
```

### Frontend: `index.html`

- Cấu trúc HTML: Header + Main content (Left panel + Right panel) + Footer
- Form để nhập dữ liệu
- Dropdown chọn mẫu
- Các nút hành động
- Vùng để hiển thị biểu đồ (vis.js)

### Frontend: `style.css`

- Reset styles
- Responsive layout (Flexbox)
- Styling cho form, buttons, boxes
- Màu sắc gradient (Purple theme)
- Mobile-friendly media queries

### Frontend: `app.js`

```javascript
// Hàm chính:
- handleSolve(): Gọi API khi nhấp "Bắt Đầu Giải"
- handleClear(): Xóa dữ liệu
- handleSampleSelect(): Tải dữ liệu mẫu
- parseVertices(): Phân tích chuỗi vertices
- parseEdges(): Phân tích chuỗi edges
- drawGraph(): Vẽ biểu đồ bằng vis.js
- displaySolutionInfo(): Hiển thị kết quả
- updateStatus(): Cập nhật thông báo trạng thái
```

---

## 🧪 Ví Dụ Thực Hành

### Ví Dụ 1: Bản Đồ Hình Vuông

**Input:**
```
Vertices: A, B, C, D
Edges: A-B, B-C, C-D, D-A
```

**Giải Thích:**
```
A --- B
|     |
D --- C
```
Đây là chu kỳ 4 đỉnh, cần 2 màu.

**Expected Output:**
```json
{
  "success": true,
  "solution": {
    "A": "color_0",
    "B": "color_1",
    "C": "color_0",
    "D": "color_1"
  },
  "num_colors": 2,
  "backtrack_count": 1
}
```

---

### Ví Dụ 2: Bản Đồ Hình Tam Giác

**Input:**
```
Vertices: A, B, C
Edges: A-B, B-C, C-A
```

**Giải Thích:**
```
A === B
 \   /
  \ /
   C
```
Đây là tam giác, cần 3 màu.

**Expected Output:**
```json
{
  "success": true,
  "solution": {
    "A": "color_0",
    "B": "color_1",
    "C": "color_2"
  },
  "num_colors": 3,
  "backtrack_count": 2
}
```

---

### Ví Dụ 3: Bản Đồ Úc (Phức Tạp)

**Input:**
```
Vertices: WA, NT, QLD, NSW, V, SA, T
Edges: WA-NT, WA-SA, NT-SA, NT-QLD, SA-QLD, SA-NSW, SA-V, QLD-NSW, NSW-V
```

**Expected Output:**
```json
{
  "success": true,
  "num_colors": 3,
  "solution": {
    "WA": "color_0",
    "NT": "color_1",
    "QLD": "color_0",
    "NSW": "color_1",
    "V": "color_0",
    "SA": "color_2",
    "T": "color_0"
  },
  "backtrack_count": 7
}
```

---

## 🔍 Troubleshooting

### ❌ Lỗi: "Failed to fetch from http://localhost:5000"

**Nguyên Nhân:** Backend chưa chạy hoặc port 5000 bị chiếm

**Giải Pháp:**
```bash
# Kiểm tra Flask chạy chưa
# (Terminal backend có dòng "Running on..."?)

# Nếu port 5000 bị chiếm, chỉnh sửa app.py:
app.run(debug=True, port=5001)  # Đổi sang port 5001

# Cập nhật frontend app.js:
const API_BASE_URL = 'http://localhost:5001';
```

---

### ❌ Lỗi: "ModuleNotFoundError: No module named 'flask'"

**Nguyên Nhân:** Flask chưa được cài đặt

**Giải Pháp:**
```bash
# Kích hoạt virtual environment (Windows)
backend\venv\Scripts\activate

# Cài đặt dependencies
pip install -r requirements.txt
```

---

### ❌ Lỗi: "CORS Error"

**Nguyên Nhân:** Frontend và Backend không trên cùng origin

**Giải Pháp:** Flask đã được cấu hình CORS, nên không có vấn đề. Nếu vẫn lỗi:
```python
# app.py
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

---

### ⚠️ Lỗi: vis.js không load được

**Nguyên Nhân:** Không kết nối Internet hoặc CDN hết service

**Giải Pháp:**
```html
<!-- Thay thế CDN link trong index.html -->
<!-- Tải offline nếu cần -->
<script src="lib/vis-network.min.js"></script>
```

---

## 📚 Tài Liệu Tham Khảo

### Sách & Bài Báo
- "Artificial Intelligence: A Modern Approach" - Russell & Norvig
- "Search Strategies and Constraint Satisfaction" - Trong AI Textbooks

### Online Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [vis.js Network Documentation](https://visjs.org/docs/network/index.html)
- [Constraint Satisfaction Problem - Wikipedia](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)

### Code References
- Google AI CSP Implementation
- MIT OpenCourseWare: AI Course

---

## 📞 Liên Hệ & Hỗ Trợ

Nếu có vấn đề hoặc câu hỏi:

1. Kiểm tra lại hướng dẫn trên
2. Xem phần Troubleshooting
3. Mở file console (F12) xem error message
4. Kiểm tra logs từ Flask server (terminal)

---

## 📄 License

Dự án này được tạo cho mục đích giáo dục.  
Tự do sử dụng, sửa đổi, và phát triển.

---

## ✅ Checklist Hoàn Thành

- ✅ Backend: Python Flask + CSP Solver với Backtracking + Heuristics
- ✅ Frontend: HTML/CSS/JS + vis.js Visualization
- ✅ API: RESTful endpoints (/api/solve, /api/samples, /api/validate)
- ✅ UI: Modern, responsive, user-friendly
- ✅ Comments: Chi tiết bằng Tiếng Việt
- ✅ Data: Mẫu dữ liệu (Australia, Europe, Simple)
- ✅ Documentation: Hướng dẫn hoàn chỉnh
- ✅ Error Handling: Xử lý lỗi toàn diện
- ✅ Performance: Optimization với Heuristics

---

**Happy Coding! 🚀🎨**

*Dự án này được phát triển theo tiêu chuẩn Clean Code và Best Practices.*