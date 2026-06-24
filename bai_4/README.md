
PHẦN 1: PHÂN TÍCH THIẾT KẾ MODULE VÀ HÀM

[MODULE 1] Tên module: utils.score_utils
- Vai trò: Xử lý logic nghiệp vụ tính toán điểm số và xếp loại sinh viên.
- Kiểu import sử dụng: Không sử dụng import module bên ngoài.

  * Hàm: calculate_average(scores)
    + Input: scores (list) - Danh sách điểm số.
    + Output: float - Điểm trung bình.
    + Mô tả luồng xử lý: Kiểm tra list rỗng, lọc bỏ các phần tử không phải dạng số 
      (int hoặc float) bằng list comprehension, tính tổng và chia cho số lượng điểm hợp lệ.

  * Hàm: classify_student(average)
    + Input: average (float) - Điểm trung bình.
    + Output: str - Chuỗi xếp loại ("Giỏi", "Khá", "Trung bình", "Yếu").
    + Mô tả luồng xử lý: Dùng chuỗi lệnh if/elif để trả về xếp loại theo các mốc điểm.

[MODULE 2] Tên module: utils.string_utils
- Vai trò: Cung cấp tiện ích xử lý và làm sạch chuỗi văn bản.
- Kiểu import sử dụng: Không sử dụng import.

  * Hàm: normalize_student_names(records)
    + Input: records (list) - Danh sách dictionary chứa thông tin sinh viên.
    + Output: Cập nhật trực tiếp tên trong list, in kết quả ra terminal.
    + Mô tả luồng xử lý: Kiểm tra list rỗng. Duyệt qua từng bản ghi, dùng split() để 
      bỏ khoảng trắng thừa, dùng " ".join() gộp lại và dùng title() để viết hoa chữ cái đầu.

[MODULE 3] Tên module: utils.random_utils
- Vai trò: Xử lý các logic sinh chuỗi ngẫu nhiên.
- Kiểu import sử dụng: import module (import random), import module as alias (import string as str_lib).

  * Hàm: generate_assignment_code()
    + Input: Không có.
    + Output: In mã bài tập ngẫu nhiên ra terminal.
    + Mô tả luồng xử lý: Ghép chuỗi chữ cái in hoa và số từ str_lib, dùng random.choices 
      để bốc ngẫu nhiên 4 ký tự, ghép thành chuỗi định dạng "PY-[Mã]".

[MODULE 4] Tên module: reports.report_generator
- Vai trò: Xử lý luồng hiển thị danh sách và xuất file báo cáo.
- Kiểu import sử dụng: from module import function, import module as alias.

  * Hàm: display_student_scores(records)
    + Input: records (list).
    + Output: In thông tin và điểm sinh viên ra terminal.
    + Mô tả luồng xử lý: Kiểm tra list rỗng. Duyệt qua dữ liệu, gọi calculate_average() 
      và classify_student() để lấy thông tin. In ra màn hình.

  * Hàm: export_learning_report(records)
    + Input: records (list).
    + Output: Ghi file learning_report.txt, in thông báo màu xanh.
    + Mô tả luồng xử lý: Tính tổng số lượng. Đếm sinh viên có ĐTB >= 5.0. Lấy thời gian 
      thực bằng datetime. Ghi kết quả vào file. Dùng colorama in thông báo màu.

[MODULE 5] Tên module: main
- Vai trò: Điểm chạm đầu vào (Entry point), điều hướng người dùng.

  * Hàm: main()
    + Input: Tương tác trực tiếp từ Terminal.
    + Output: Chạy luồng chương trình.
    + Mô tả luồng xử lý: Chạy vòng lặp while True, in Menu. Dùng try-except bẫy lỗi 
      ValueError. Nhánh if-elif điều hướng lựa chọn tới các module chức năng.
