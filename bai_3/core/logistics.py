import math

def display_schedule(flights):
    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    for i, f in enumerate(flights, 1):
        water_boxes = math.ceil(f["passengers"] / 10)
        print(f"{i}. Mã: {f['flight_id']} | Khởi hành: {f['depart_time']} | Số khách: {f['passengers']} | Dự phòng: {water_boxes} thùng nước.")