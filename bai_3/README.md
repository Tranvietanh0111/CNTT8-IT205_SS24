
1. Sơ đồ cấu trúc cây thư mục (Folder Tree):
   rikkei_aviation/
   ├── core/
   │   ├── __init__.py
   │   ├── logistics.py
   │   └── manager.py
   ├── utils/
   │   ├── __init__.py
   │   ├── file_helper.py
   │   └── time_helper.py
   └── main.py

2. Lý do hạn chế sử dụng 'from math import *':
   - Tác hại lớn nhất là gây ô nhiễm không gian tên (Namespace Pollution). Lệnh này nạp
     toàn bộ các biến và hàm của thư viện vào file hiện tại, có thể vô tình ghi đè lên
     các biến/hàm trùng tên đang có sẵn trong mã nguồn. 
   - Code mất tính tường minh, người đọc không biết một hàm cụ thể đang được gọi ra 
     từ thư viện nào. Giải pháp tốt nhất là 'import math' hoặc 'from math import ceil'.
