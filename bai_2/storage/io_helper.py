import os

def safe_create_dir(path):
    """Tạo thư mục an toàn, bỏ qua nếu thư mục đã tồn tại."""
    os.makedirs(path, exist_ok=True)