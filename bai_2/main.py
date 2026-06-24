
# 1. Tác hại của việc sử dụng 'from datetime import *':
#    - Gây ô nhiễm không gian tên (Namespace Pollution).
#    - Xung đột biến global: Nếu có biến 'time = 120', lệnh import trên (nếu chạy sau) 
#      sẽ nạp lớp 'time' của thư viện ghi đè lên biến, làm mất giá trị 120. Ngược lại, 
#      nếu biến khai báo sau, số 120 sẽ đè lên hàm của hệ thống, gây lỗi khi gọi hàm time().
# 
# 2. Hàm tối ưu hơn os.mkdir() để tạo thư mục lồng nhau:
#    - Hàm đề xuất: os.makedirs(path, exist_ok=True)
#    - Ưu điểm: Tự động khởi tạo toàn bộ chuỗi thư mục cha/con và bỏ qua một cách an toàn 
#      (không văng lỗi FileExistsError) nếu thư mục đích đã tồn tại trên ổ đĩa.


from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

def main():
    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
    
    safe_create_dir("media_vault/audio")
    safe_create_dir("media_vault/video")
    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    print("-" * 75)
    
    raw_files = [
        {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
        {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
        {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
    ]
    
    success_count = 0
    total_count = len(raw_files)
    
    for file_info in raw_files:
        filename = file_info["filename"]
        size_bytes = file_info["size_bytes"]
        upload_date_str = file_info["upload_at"]
        
        print(f"[TỆP TIN: {filename}]")
        
        valid_date = parse_and_inspect_date(upload_date_str)
        if not valid_date:
            print(f" + Trạng thái phân loại:  THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_date_str}' không tồn tại)\n")
            continue
            
        blocks = calculate_disk_blocks(size_bytes)
        
        if filename.endswith(".mp3"):
            category = "audio"
        else:
            category = "video"
            
        print(f" + Dung lượng thực tế: {size_bytes:,} Bytes")
        print(f" + Số khối phân vùng (4KB Block): {blocks} Blocks")
        print(f" + Trạng thái phân loại:  HỢP LỆ (Lưu trữ vào thư mục '{category}')\n")
        
        success_count += 1
        
    print("========================================================")
    print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{total_count} tệp tin thành công. Hệ thống ổn định.")

if __name__ == "__main__":
    main()