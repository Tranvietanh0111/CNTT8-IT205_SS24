# 1. 'from math import *' là Anti-pattern vì gây ô nhiễm namespace, 
# dễ trùng và ghi đè tên hàm mà không cảnh báo, khó debug.
# -> Khắc phục: Dùng 'from math import sqrt, sin, cos, radians' hoặc 'import math'.
# 2. Để biến thư mục thành Package cần tệp '__init__.py'. 
# Vai trò: Đánh dấu package cho Python nhận diện và cấu hình khởi tạo.

from datetime import datetime
from file_helper import create_log_dir
from geo_calculator import calculate_distance
from time_estimator import predict_eta

shipments = [
    {
        "id": "TRK-001", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 10.8231, "to_lon": 106.6297, 
        "depart": "2026-06-10 08:00:00", "deadline": "2026-06-11 12:00:00"
    }, 
    {
        "id": "TRK-002", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 16.0544, "to_lon": 108.2022, 
        "depart": "2026-06-10 09:30:00", "deadline": "2026-06-10 15:00:00"
    }, 
]

def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
    create_log_dir("logs")
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)
    
    for s in shipments:
        distance = calculate_distance(s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])
        eta = predict_eta(s["depart"], distance, speed=60.0)
        deadline_dt = datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")
        
        if eta <= deadline_dt:
            status = "AN TOÀN (Kịp tiến độ trước deadline)"
        else:
            status = f"CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline_dt.strftime('%H:%M:%S')})"
            
        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" + Trạng thái: {status}\n")
        
    print("========================================================")

if __name__ == "__main__":
    main()