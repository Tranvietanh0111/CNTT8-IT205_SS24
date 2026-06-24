from utils.score_utils import calculate_average, classify_student
import datetime as dt
from colorama import Fore, Style, init

init(autoreset=True)

def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for i, record in enumerate(records, 1):
        scores = record.get("scores", [])
        avg = calculate_average(scores)
        classification = classify_student(avg)
        print(f"{i}. [{record['student_id']}] {record['name']} | Điểm: {scores} | ĐTB: {avg:.2f} - {classification}")
    print("-" * 33)

def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    total_students = len(records)
    passed = 0
    
    for record in records:
        avg = calculate_average(record.get("scores", []))
        if avg >= 5.0:
            passed += 1
            
    failed = total_students - passed
    
    current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_content = (
        f"BÁO CÁO HỌC TẬP\n"
        f"Thời gian tạo: {current_time}\n"
        f"Tổng số sinh viên: {total_students}\n"
        f"Số sinh viên đạt yêu cầu: {passed}\n"
        f"Số sinh viên cần cải thiện: {failed}\n"
    )
    
    with open("learning_report.txt", "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print("--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {passed}")
    print(f"Số sinh viên cần cải thiện: {failed}")
    print(Fore.GREEN + ">> Đã xuất báo cáo ra file learning_report.txt" + Style.RESET_ALL)