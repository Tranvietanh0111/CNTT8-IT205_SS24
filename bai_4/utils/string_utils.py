def normalize_student_names(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    
    print("--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for record in records:
        name = record.get("name", "")
        normalized_name = " ".join(name.split()).title()
        record["name"] = normalized_name
        print(f"{record['student_id']}: {record['name']}")
    
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")