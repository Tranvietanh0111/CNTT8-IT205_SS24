from datetime import datetime, timedelta

def calculate_eta(flights):
    print("----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    flight_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    
    target_flight = None
    for f in flights:
        if f["flight_id"].upper() == flight_id:
            target_flight = f
            break
            
    if not target_flight:
        print("Lỗi: Không tìm thấy mã chuyến bay!")
        return
        
    depart_time = datetime.strptime(target_flight["depart_time"], "%Y-%m-%d %H:%M:%S")
    eta = depart_time + timedelta(minutes=target_flight["duration_min"])
    
    print(f"-> Chuyến bay {target_flight['flight_id']} cất cánh lúc: {target_flight['depart_time']}")
    print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")