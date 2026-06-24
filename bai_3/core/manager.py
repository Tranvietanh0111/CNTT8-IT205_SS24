from datetime import datetime

def check_duplicate_id(flight_id, flight_list):
    for f in flight_list:
        if f["flight_id"].upper() == flight_id.strip().upper():
            return True
    return False

def add_new_flight(flights):
    print("----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    flight_id = input("Nhập mã chuyến bay: ").strip().upper()
    
    if check_duplicate_id(flight_id, flights):
        print("Lỗi: Mã chuyến bay đã tồn tại!")
        return
    
    try:
        passengers = int(input("Nhập số lượng hành khách: "))
    except ValueError:
        print("Lỗi: Số lượng hành khách không hợp lệ!")
        return
        
    depart_time_str = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ")
    try:
        datetime.strptime(depart_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS")
        return
        
    try:
        duration_min = int(input("Nhập số phút bay: "))
    except ValueError:
        print("Lỗi: Số phút bay không hợp lệ!")
        return
        
    new_flight = {
        "flight_id": flight_id,
        "passengers": passengers,
        "depart_time": depart_time_str,
        "duration_min": duration_min
    }
    flights.append(new_flight)
    print(f">> Thêm chuyến bay {flight_id} thành công!")