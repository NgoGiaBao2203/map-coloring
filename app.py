"""
Author 1: Hồ Văn Tài
Author 2: Ngô Gia Bảo
Created: 09/05/2026
Last Updated: 09/05/2026
Version: 1.0.0
"""
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import os

from image_processor import process_image
from solver import solve_map

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

# =========================
# HOME
# =========================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# =========================
# UPLOAD + SOLVE
# =========================

@app.route(
    "/upload",
    methods=["POST"]
)

def upload():

    if "image" not in request.files:

        return jsonify({

            "error": "Không có file"
        }), 400

    file = request.files["image"]

    path = os.path.join(
        UPLOAD_FOLDER,
        "map.png"
    )

    os.makedirs(os.path.dirname(path), exist_ok=True)

    file.save(path)

    print("Đã lưu ảnh")

    # xử lý ảnh
    regions = process_image(path)

    if regions is None:

        return jsonify({

            "error": "Ảnh phải có nền trắng và viền đen"
        }), 400

    # solve CSP
    solution, min_colors, steps = solve_map(
        regions
    )

    if solution is None:
        return jsonify({
            "error": "Không thể tô màu ảnh này. Ảnh có thể quá phức tạp, bị nhiễu, hoặc không đáp ứng yêu cầu (nền trắng, viền đen rõ). Hãy thử PNG hoặc cải thiện chất lượng ảnh."
        }), 400

    # gán màu cuối
    for node in solution:

        regions[node]["color"] = (
            solution[node]
        )

    return jsonify({

        "regions": regions,

        "steps": steps,

        "min_colors": min_colors
    })

# =========================

if __name__ == "__main__":

    app.run(debug=True)