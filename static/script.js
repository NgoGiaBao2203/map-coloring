/*
Author: Dương Trí Thành
Created: 09/05/2026
Last Updated: 10/05/2026
Version: 1.1.0
*/

/* ========================================== */
/* 1. KHAI BÁO BIẾN TOÀN CỤC                  */
/* ========================================== */
let currentRegions = {}; // Lưu trữ trạng thái màu hiện tại của các vùng
let finalRegions = {}; // Lưu trữ kết quả cuối cùng từ server trả về
let steps = []; // Mảng lưu trữ các bước chạy thuật toán (logs)
let stepIndex = 0; // Chỉ số bước đang chạy hiện tại
let isPlaying = false; // Trạng thái có đang chạy animation hay không
let uploadedFile = null; // Biến lưu trữ file ảnh do người dùng tải lên

/* ========================================== */
/* 2. KHỞI TẠO VÀ LẮNG NGHE SỰ KIỆN           */
/* ========================================== */
// Khi trang web vừa tải xong sẽ chạy hàm này
document.addEventListener("DOMContentLoaded", () => {
  setupEventListeners();
});

// Hàm gán sự kiện cho input file
function setupEventListeners() {
  const imageInput = document.getElementById("imageInput");
  imageInput.addEventListener("change", (e) => {
    uploadedFile = e.target.files[0];
    if (uploadedFile) {
      displayFileName(uploadedFile.name); // Cập nhật tên file lên nút
      displayImagePreview(uploadedFile); // Hiển thị ảnh gốc lên giao diện
    }
  });
}

// Hàm đổi tên label thành tên file đã chọn
function displayFileName(fileName) {
  const label = document.querySelector(".file-label");
  const shortName =
    fileName.length > 20 ? fileName.substring(0, 20) + "..." : fileName;
  label.textContent = `✅ ${shortName}`;
}

/* ========================================== */
/* 3. XỬ LÝ ẢNH VÀ TẢI LÊN SERVER             */
/* ========================================== */
// Hàm hiển thị ảnh preview bên cạnh canvas
function displayImagePreview(file) {
  const reader = new FileReader();
  reader.onload = (e) => {
    const preview = document.getElementById("imagePreview");
    const img = document.getElementById("previewImg");
    const mapComparison = document.getElementById("mapComparison");

    img.onload = () => {
      setCanvasSize(img.naturalWidth, img.naturalHeight);
    };

    img.src = e.target.result;
    preview.style.display = "flex"; // Hiện vùng chứa ảnh

    // Thêm class để CSS tự động chia làm 2 cột (Ảnh gốc & Canvas)
    mapComparison.classList.add("has-image");
  };
  reader.readAsDataURL(file);
}

// Đồng bộ kích thước canvas với kích thước ảnh gốc
function setCanvasSize(width, height) {
  const canvas = document.getElementById("canvas");
  canvas.width = width;
  canvas.height = height;
}

// Hàm gửi ảnh lên Backend qua API /upload
function uploadImage() {
  if (!uploadedFile) {
    alert("Vui lòng chọn ảnh bản đồ trước khi giải!");
    return;
  }

  const formData = new FormData();
  formData.append("image", uploadedFile);

  const btn = document.getElementById("solveBtn");
  const originalText = btn.innerHTML;

  // Vô hiệu hóa nút và đổi text thành Đang xử lý
  btn.disabled = true;
  btn.innerHTML = "Đang xử lý...";

  // Ẩn badge thông báo đi nếu trước đó đã từng giải
  document.getElementById("info").style.display = "none";

  // Gọi API
  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then(async (res) => {
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || "Lỗi khi tải ảnh lên");
      }
      if (data.error) {
        throw new Error(data.error);
      }
      return data;
    })
    .then((data) => {
      // Nhận dữ liệu và gán vào biến toàn cục
      currentRegions = JSON.parse(JSON.stringify(data.regions));
      finalRegions = data.regions;
      steps = data.steps;
      stepIndex = 0;

      // Reset màu sắc các vùng về rỗng để bắt đầu vẽ từ đầu
      for (let key in currentRegions) {
        delete currentRegions[key].color;
      }

      // Cập nhật UI
      updateInfo(data.min_colors);
      clearLogs();
      drawMap(currentRegions);

      // Bắt đầu chạy hiệu ứng từng bước
      playSteps();

      // Khôi phục trạng thái nút bấm
      btn.disabled = false;
      btn.innerHTML = originalText;
    })
    .catch((error) => {
      console.error("Error:", error);
      alert(`Đã xảy ra lỗi: ${error.message}`);
      btn.disabled = false;
      btn.innerHTML = originalText;
    });
}

/* ========================================== */
/* 4. VẼ CANVAS BẢN ĐỒ                        */
/* ========================================== */
// Hàm vẽ các vùng đa giác lên thẻ Canvas
function drawMap(regions) {
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");

  // Xóa trắng toàn bộ khung vẽ trước khi vẽ mới
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Lặp qua từng khu vực (region) để vẽ
  for (let key in regions) {
    const region = regions[key];
    const points = region.points;

    if (points.length === 0) continue;

    // Bắt đầu vẽ đường viền đa giác
    ctx.beginPath();
    ctx.moveTo(points[0][0], points[0][1]);

    for (let i = 1; i < points.length; i++) {
      ctx.lineTo(points[i][0], points[i][1]);
    }
    ctx.closePath();

    // Tô màu vùng (nếu chưa có màu do thuật toán cấp thì tô xám nhạt mặc định)
    ctx.fillStyle = region.color || "#e5e7eb";
    ctx.fill();

    // Vẽ đường viền xám đậm ngăn cách các vùng
    ctx.strokeStyle = "#4b5563";
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Vẽ Text (tên khu vực)
    if (points.length > 0) {
      const labelX = points[0][0];
      const labelY = points[0][1];

      ctx.font = "bold 14px Nunito, Arial";
      ctx.textBaseline = "top";
      ctx.textAlign = "left";

      // Tạo viền trắng quanh chữ để tránh bị chìm khi tô màu nền đậm
      ctx.strokeStyle = "white";
      ctx.lineWidth = 3;
      ctx.strokeText(key, labelX + 5, labelY + 5);

      // Vẽ chữ đen lên trên
      ctx.fillStyle = "#111827";
      ctx.fillText(key, labelX + 5, labelY + 5);
    }
  }
}

/* ========================================== */
/* 5. HIỆU ỨNG CHẠY TỪNG BƯỚC (ANIMATION)     */
/* ========================================== */
// Hàm chạy tự động các bước của thuật toán CSP
function playSteps() {
  if (isPlaying) return;
  isPlaying = true;

  function executeNextStep() {
    // Nếu đã chạy hết các bước
    if (stepIndex >= steps.length) {
      addLog("Đã tô màu xong toàn bộ bản đồ!", "complete");
      updateStepCounter();
      isPlaying = false;
      return; // Dừng đệ quy
    }

    const step = steps[stepIndex];

    // Ghi log ra màn hình bên phải
    addLog(step.message, getLogType(step.type));

    // Xử lý logic tô màu theo loại bước (assign là tô, backtrack là quay lui/xóa màu)
    if (step.type === "assign") {
      currentRegions[step.node].color = step.color;
    } else if (step.type === "backtrack") {
      delete currentRegions[step.node].color;
    }

    // Cập nhật lại giao diện Canvas
    drawMap(currentRegions);

    // Tăng biến đếm và cập nhật số bước lên UI
    stepIndex++;
    updateStepCounter();

    // Đặt thời gian nghỉ (500ms) trước khi thực hiện bước tiếp theo
    setTimeout(executeNextStep, 500);
  }

  // Khởi động vòng lặp
  executeNextStep();
}

/* ========================================== */
/* 6. QUẢN LÝ GHI CHÚ LỊCH SỬ (LOGS)          */
/* ========================================== */
// Chuyển đổi loại step sang class CSS tương ứng
function getLogType(stepType) {
  switch (stepType) {
    case "assign":
      return "assign";
    case "backtrack":
      return "backtrack";
    default:
      return "default";
  }
}

// Thêm một dòng thông báo vào thẻ div #logs
function addLog(text, type = "default") {
  const logsContainer = document.getElementById("logs");
  const div = document.createElement("div");
  div.className = `log-item ${type}`;

  // In đậm tên các Node và in màu tương ứng cho từ khóa màu sắc
  let formattedText = text;
  formattedText = formattedText.replace(
    /\b([A-Z])\b(?![\w\s]*[a-z])/g,
    '<span class="log-highlight">$1</span>',
  );
  formattedText = formattedText.replace(
    /colors?:\s*(\w+)/gi,
    (match, color) =>
      `color: <span style="color: ${color}; font-weight: bold;">⬤ ${color}</span>`,
  );

  div.innerHTML = formattedText;
  logsContainer.appendChild(div);

  // Tự động cuộn thanh cuộn xuống dòng mới nhất
  logsContainer.scrollTop = logsContainer.scrollHeight;
}

// Xóa sạch lịch sử cũ
function clearLogs() {
  document.getElementById("logs").innerHTML = "";
}

/* ========================================== */
/* 7. HÀM TIỆN ÍCH VÀ CẬP NHẬT UI             */
/* ========================================== */
// Hiện Badge chứa kết quả số màu lên góc trái
function updateInfo(minColors) {
  const infoBadge = document.getElementById("info");
  infoBadge.style.display = "inline-block";
  infoBadge.textContent = `🎯 Số màu tối thiểu cần dùng: ${minColors}`;
}

// Cập nhật số đếm bước chạy hiện tại
function updateStepCounter() {
  document.getElementById("stepCount").textContent = stepIndex;
  document.getElementById("totalSteps").textContent = steps.length;
}

// Hàm xử lý khi người dùng nhấn nút "Chạy lại từ đầu"
function resetVisualization() {
  if (steps.length === 0) {
    alert("Chưa có dữ liệu để chạy lại!");
    return;
  }

  // Khôi phục các biến trạng thái về ban đầu
  stepIndex = 0;
  isPlaying = false;
  currentRegions = JSON.parse(JSON.stringify(finalRegions));

  // Xóa toàn bộ màu trong currentRegions
  for (let key in currentRegions) {
    delete currentRegions[key].color;
  }

  // Xóa log và vẽ lại bản đồ trắng
  clearLogs();
  drawMap(currentRegions);
  updateStepCounter();

  // Bắt đầu chạy lại hiệu ứng sau 0.3s
  setTimeout(() => {
    playSteps();
  }, 300);
}

// Hàm bỏ qua animation và hiển thị kết quả ngay
function skipToResult() {
  if (steps.length === 0) {
    alert("Chưa có dữ liệu!");
    return;
  }

  // Dừng animation nếu đang chạy
  isPlaying = false;

  // Đặt lại từ đầu
  stepIndex = 0;
  currentRegions = JSON.parse(JSON.stringify(finalRegions));

  // Xóa toàn bộ màu
  for (let key in currentRegions) {
    delete currentRegions[key].color;
  }

  // Xóa log
  clearLogs();

  // Lặp qua tất cả các bước mà không delay
  for (let i = 0; i < steps.length; i++) {
    const step = steps[i];

    // Chỉ ghi log các bước assign và backtrack, bỏ qua "try" và "select" để log gọn gàng
    if (
      step.type === "assign" ||
      step.type === "backtrack" ||
      step.type === "success" ||
      step.type === "info"
    ) {
      addLog(step.message, getLogType(step.type));
    }

    // Áp dụng logic tô màu
    if (step.type === "assign") {
      currentRegions[step.node].color = step.color;
    } else if (step.type === "backtrack") {
      delete currentRegions[step.node].color;
    }
  }

  // Cập nhật số bước
  stepIndex = steps.length;
  updateStepCounter();

  // Vẽ kết quả cuối cùng
  drawMap(currentRegions);
}
