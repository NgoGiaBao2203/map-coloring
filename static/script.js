const regions = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];
let delay = 350;

function log(msg) {
  const logDiv = document.getElementById("log");
  logDiv.innerHTML += msg + "<br>";
  logDiv.scrollTop = logDiv.scrollHeight;
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

function resetMap() {
  document.getElementById("log").innerHTML = "";
  regions.forEach((r) => (document.getElementById(r).style.fill = "white"));
}

// Gọi API sang Python
async function startSolve() {
  resetMap();
  log("--- Đang kết nối tới Python Backend ---");

  try {
    // Lấy dữ liệu các bước giải từ Python
    const response = await fetch("/solve");
    const data = await response.json();

    if (data.success) {
      log("--- Thuật toán chạy xong, bắt đầu mô phỏng ---");

      // Chạy vòng lặp để tạo animation từ dữ liệu Python trả về
      for (let step of data.steps) {
        log(step.msg);

        // Cập nhật màu lên bản đồ
        if (
          step.type === "try" ||
          step.type === "assign" ||
          step.type === "backtrack" ||
          step.type === "invalid"
        ) {
          document.getElementById(step.region).style.fill = step.color;
        }

        await sleep(delay); // Dừng 1 chút để nhìn rõ hiệu ứng
      }

      log("--- Hoàn thành ---");
    }
  } catch (error) {
    log("Lỗi: Không thể kết nối tới server Python. Bạn đã chạy app.py chưa?");
    console.error(error);
  }
}
