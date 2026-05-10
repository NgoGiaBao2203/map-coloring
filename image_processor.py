"""
Author 1: Hồ Văn Tài
Created: 09/05/2026
Last Updated: 09/05/2026
Version: 1.0.0
"""

import cv2
import numpy as np
import os

# =========================
# KIỂM TRA NỀN ẢNH
# =========================
def is_white_background_black_border(gray):
    """
    Kiểm tra ảnh có nền trắng và viền đen.

    Args:
        gray (numpy.ndarray): Ảnh xám đầu vào.

    Returns:
        bool: True nếu ảnh thỏa điều kiện nền trắng và viền đen. False nếu không.
    """
    h, w = gray.shape
    margin = max(1, min(h, w) // 20)  # Lề kiểm tra (5% cạnh nhỏ nhất)

    # Lấy pixel ở 4 biên
    top = gray[:margin, :].flatten()
    bottom = gray[-margin:, :].flatten()
    left = gray[:, :margin].flatten()
    right = gray[:, -margin:].flatten()

    border_pixels = np.concatenate(
        [top, bottom, left, right]
    )

    # Tỷ lệ pixel trắng ở biên (phải >90%)
    white_ratio = np.mean(border_pixels >= 240)
    # Tỷ lệ pixel đen trong toàn ảnh (phải >0.1% để có viền)
    black_ratio = np.mean(gray <= 50)

    if white_ratio < 0.9:
        return False

    if black_ratio < 0.001:
        return False

    return True

# =========================
# XỬ LÝ ẢNH VÀ TẠO GRAPH
# =========================
def process_image(image_path):
    """
    Đọc ảnh và xây dựng cấu trúc vùng bản đồ cùng danh sách láng giềng.

    Args:
        image_path (str): Đường dẫn tới file ảnh đầu vào.

    Returns:
        dict hoặc None: Dữ liệu vùng nếu xử lý thành công, None nếu ảnh không hợp lệ.
    """

    # =========================
    # ĐỌC ẢNH
    # =========================

    img = cv2.imread(image_path)

    if img is None:
        print("Không đọc được ảnh!")
        return None

    print("Đọc ảnh thành công")

    # =========================
    # CHUYỂN XÁM VÀ KIỂM TRA
    # =========================

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    if not is_white_background_black_border(gray):
        print("Ảnh không phải nền trắng viền đen.")
        return None

    # =========================
    # THRESHOLD ĐỂ TÁCH VIỀN
    # =========================

    _, thresh = cv2.threshold(
        gray,
        200,  # Ngưỡng
        255,  # Giá trị max
        cv2.THRESH_BINARY_INV  # Đảo ngược (viền đen thành trắng)
    )

    # =========================
    # TÌM ĐƯỜNG VIỀN (CONTOURS)
    # =========================

    contours, hierarchy = cv2.findContours(
        thresh,
        cv2.RETR_TREE,  # Tìm tất cả contours
        cv2.CHAIN_APPROX_SIMPLE  # Giản hóa điểm
    )

    print("Tổng contour:", len(contours))

    # =========================
    # TÌM CONTOUR LỚN NHẤT (NỀN)
    # =========================

    max_area = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area

    # =========================
    # LỌC CONTOUR (LOẠI NỀN, QUÁ NHỎ)
    # =========================

    filtered = []

    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        print(f"Contour {i} area =", area)

        if area < max_area and area > 500:  # Vùng nhỏ hơn nền, lớn hơn 500px
            filtered.append(cnt)

    contours = filtered

    print("Số vùng:", len(contours))

    # =========================
    # ẢNH DEBUG (VẼ CONTOURS)
    # =========================

    debug = img.copy()

    cv2.drawContours(
        debug,
        contours,
        -1,  # Vẽ tất cả
        (0, 0, 255),  # Màu đỏ
        3  # Độ dày
    )

    os.makedirs("static/debug", exist_ok=True)

    cv2.imwrite(
        "static/debug/debug_contours.png",
        debug
    )

    print("Đã lưu debug image")

    # =========================
    # TẠO GRAPH (ĐỒ THỊ LÁNG GIỀNG)
    # =========================

    graph = {}

    for i in range(len(contours)):
        graph[i] = []  # Mỗi node có list láng giềng

    # =========================
    # HÀM KIỂM TRA LÁNG GIỀNG
    # =========================

    def is_neighbor(cnt1, cnt2):
        # Kiểm tra 2 contours có kề nhau không dựa trên bounding box
        x1, y1, w1, h1 = cv2.boundingRect(cnt1)
        x2, y2, w2, h2 = cv2.boundingRect(cnt2)

        padding = 10  # Khoảng cách cho phép

        if (
            x1 < x2 + w2 + padding and
            x1 + w1 + padding > x2 and
            y1 < y2 + h2 + padding and
            y1 + h1 + padding > y2
        ):
            return True

        return False

    # =========================
    # TẠO CẠNH TRONG GRAPH
    # =========================

    for i in range(len(contours)):
        for j in range(len(contours)):
            if i != j:
                if is_neighbor(
                    contours[i],
                    contours[j]
                ):
                    graph[i].append(j)  # Thêm láng giềng

    # =========================
    # IN GRAPH RA CONSOLE
    # =========================

    print("\n===== GRAPH =====")

    for node in graph:
        print(
            f"{node} -> {graph[node]}"
        )

    print("=================\n")

    # =========================
    # XUẤT DỮ LIỆU VÙNG
    # =========================

    regions = {}

    for i, cnt in enumerate(contours):
        points = []
        for p in cnt:
            x = int(p[0][0])
            y = int(p[0][1])
            points.append([x, y])

        regions[i] = {
            "neighbors": graph[i],  # Danh sách láng giềng
            "points": points  # Điểm của contour
        }

    return regions