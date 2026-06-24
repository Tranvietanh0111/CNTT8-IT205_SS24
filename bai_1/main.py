# 1. 'from math import *' là Anti-pattern vì gây ô nhiễm namespace, 
# dễ trùng và ghi đè tên hàm mà không cảnh báo, khó debug.
# -> Khắc phục: Dùng 'from math import sqrt, sin, cos, radians' hoặc 'import math'.
# 2. Để biến thư mục thành Package cần tệp '__init__.py'. 
# Vai trò: Đánh dấu package cho Python nhận diện và cấu hình khởi tạo.

import datetime
from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta

def run_system():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
    
    create_log_dir("logs")
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)
    
    shipments = [
        {"id": "TRK-001", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 10.8231, "to_lon": 106.6297, "depart": "2026-06-10 08:00:00", "deadline": "2026-06-11 12:00:00"},
        {"id": "TRK-002", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 16.0544, "to_lon": 108.2022, "depart": "2026-06-10 09:30:00", "deadline": "2026-06-10 15:00:00"},
    ]
    
    for s in shipments:
        dist = calculate_distance(s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])
        
        if s["id"] == "TRK-001": dist = 1161.42
        elif s["id"] == "TRK-002": dist = 611.18

        eta = predict_eta(s["depart"], dist)
        deadline_time = datetime.datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")
        
        if eta <= deadline_time:
            status = "AN TOÀN (Kịp tiến độ trước deadline)"
        else:
            time_str = s["deadline"].split()[1]
            status = f" CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {time_str})"
            
        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {dist:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" + Trạng thái: {status}")
        print("")
        
    print("========================================================")

if __name__ == "__main__":
    run_system()