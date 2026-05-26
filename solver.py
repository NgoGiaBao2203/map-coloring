"""
Author 1: Ngô Gia Bảo
Created: 09/05/2026
Last Updated: 09/05/2026
Version: 1.0.0
"""

import time

ALL_COLORS = ["red", "green", "blue", "yellow"]

# =========================
# KIỂM TRA HỢP LỆ (VALID)
# =========================
def is_valid(node: str, color: str, assignment: dict, graph: dict) -> bool:
    """
    Kiểm tra tính hợp lệ khi gán màu cho một đỉnh (node) trong đồ thị. 
    Hàm đảm bảo rằng việc gán 'color' cho 'node' không vi phạm ràng buộc cơ bản:
    Không có bất kỳ hai đỉnh kề nhau (láng giềng) nào mang cùng một màu.
    Args:
        node (str): Đỉnh hiện tại đang được xét để gán màu.
        color (str): Màu sắc dự định sẽ gán cho đỉnh này.
        assignment (dict): Dictionary lưu trữ trạng thái hiện tại (các đỉnh đã có màu). 
                           Ví dụ: {'Node_A': 'Red', 'Node_B': 'Blue'}.
        graph (dict): Cấu trúc đồ thị, chứa thông tin các đỉnh và danh sách kề.
    Returns:
        bool: True nếu gán màu hợp lệ. False nếu vi phạm (trùng màu với láng giềng).
    """
    ## Lấy danh sách láng giềng của node từ đồ thị
    neighbors = graph[node]["neighbors"]

    for neighbor in neighbors:
        # Chỉ kiểm tra các láng giềng đã tồn tại trong danh sách được gán màu
        if neighbor in assignment:
            # Nếu láng giềng đã mang màu giống hệt màu đang muốn gán -> Vi phạm
            if assignment[neighbor] == color:
                return False  
    return True

# =========================
# HEURISTIC ĐỘ (DEGREE HEURISTIC)
# =========================
def select_unassigned_variable(assignment: dict, graph: dict) -> str:
    """
    Chọn một đỉnh chưa được tô màu dựa trên chiến thuật Degree Heuristic.
    Ưu tiên chọn đỉnh có nhiều láng giềng (nhiều ràng buộc) nhất để gán màu trước.

    Args:
        assignment (dict): Dictionary chứa các đỉnh đã được gán màu.
        graph (dict): Cấu trúc đồ thị chứa thông tin các đỉnh và láng giềng.

    Returns:
        str: Tên của vùng (node) chưa được gán màu và có số láng giềng lớn nhất.
    """
    # 1. Lọc ra danh sách tất cả các đỉnh chưa được gán màu
    unassigned = []
    for node in graph:
        if node not in assignment:
            unassigned.append(node)

    # 2. Tìm và trả về đỉnh có số lượng láng giềng nhiều nhất
    # Dùng hàm max() kết hợp với key để đếm số láng giềng
    return max(
        unassigned,
        key=lambda x: len(graph[x]["neighbors"])
    )

# =========================
# BACKTRACKING
# =========================
def backtrack( assignment, graph, colors, steps):
    """
    Hàm đệ quy sử dụng thuật toán Quay lui (Backtracking) để tìm lời giải tô màu đồ thị.
    Hàm sẽ thử từng màu cho từng vùng, nếu bế tắc sẽ quay lui để thử màu khác.
    Args:
        assignment (dict): Dictionary lưu trạng thái các vùng đã được gán màu.
        graph (dict): Cấu trúc đồ thị chứa các vùng và danh sách láng giềng.
        colors (list): Danh sách các màu có thể sử dụng.
        steps (list): Mảng lưu lịch sử các bước (select, try, assign, backtrack) để vẽ UI.
    Returns:
        dict hoặc None: Trả về trạng thái assignment hoàn chỉnh nếu tìm được lời giải. 
                        Trả về None nếu không tìm thấy lời giải hợp lệ.
    """
    # Thuật toán backtracking để tìm lời giải

    # Nếu đã gán hết biến, hoàn thành
    if len(assignment) == len(graph):
        return assignment

    # Chọn biến chưa gán theo heuristic
    # (Ưu tiên lôi vùng rắc rối nhất - nhiều láng giềng nhất ra tô màu trước)
    node = select_unassigned_variable(
        assignment,
        graph
    )

    # Ghi log: Đánh dấu bước chọn vùng để phục vụ cho việc vẽ UI/theo dõi
    steps.append({
        "type": "select",
        "node": node,
        "message": f"Chọn vùng {node}"
    })

    # Thử từng màu trong danh sách các màu cho phép
    for color in colors:
        
        # Ghi log: Ghi nhận hành động đang thử nghiệm một màu mới
        steps.append({
            "type": "try",
            "node": node,
            "color": color,
            "message": f"Thử {color} cho vùng {node}"
        })

        # Gọi hàm is_valid để kiểm tra màu này có bị trùng với láng giềng không
        if is_valid(
            node,
            color,
            assignment,
            graph
        ):
            # Gán màu tạm thời (BƯỚC TIẾN: Thử bôi màu này lên bản đồ)
            assignment[node] = color

            # Ghi log: Xác nhận gán màu hợp lệ
            steps.append({
                "type": "assign",
                "node": node,
                "color": color,
                "message": f"Gán {color} cho vùng {node}"
            })

            # Đệ quy tiếp (BƯỚC ĐI SÂU: Gọi lại chính hàm này để tô màu cho vùng tiếp theo)
            result = backtrack(
                assignment,
                graph,
                colors,
                steps
            )

            # Nếu nhận được kết quả khác None -> Đã giải xong toàn bộ bản đồ!
            if result is not None:
                return result

            # Quay lui: xóa gán và thử màu khác
            # (BƯỚC LÙI: Nếu chạy đến đây tức là bị ngõ cụt ở các bước sau, 
            # phải xóa màu vừa gán để vòng lặp for chuyển sang thử màu tiếp theo)
            del assignment[node]

            # Ghi log: Đánh dấu hành động rút lui
            steps.append({
                "type": "backtrack",
                "node": node,
                "message": f"Quay lui vùng {node}"
            })

    return None  # Không tìm thấy lời giải với số màu này (Thất bại sau khi đã thử mọi màu)

# =========================
# HÀM GIẢI CHÍNH
# =========================

def solve_map(graph):
    """
    Hàm điều phối chính để giải bài toán tô màu bản đồ.
    Thuật toán sẽ thử tìm lời giải với số lượng màu tăng dần (từ 1 màu, 2 màu...) 
    để đảm bảo tìm ra phương án tối ưu (sử dụng ít màu nhất có thể).

    Args:
        graph (dict): Cấu trúc đồ thị chứa các vùng và danh sách láng giềng.

    Returns:
        tuple: Gồm 3 giá trị (result, k, steps)
            - result (dict/None): Bản đồ đã tô màu hoàn chỉnh, hoặc None nếu thất bại.
            - k (int): Số lượng màu tối thiểu đã dùng để giải thành công.
            - steps (list): Lịch sử toàn bộ quá trình chạy thuật toán để mô phỏng UI.
    """
    # Giải bài toán với số màu tăng dần từ 1 đến 4

    steps = []

    for k in range(1, len(ALL_COLORS) + 1):
        colors = ALL_COLORS[:k]  # Lấy k màu đầu

        steps.append({
            "type": "info",
            "message": f"Đang thử với {k} màu"
        })

        result = backtrack(
            {},  # Bắt đầu với assignment rỗng
            graph,
            colors,
            steps
        )

        if result is not None:
            steps.append({
                "type": "success",
                "message": "Đã tìm thấy lời giải"
            })

            return result, k, steps  # Trả về lời giải, số màu, steps

    return None, 0, steps  # Không giải được