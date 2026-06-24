from datetime import datetime

def parse_and_inspect_date(date_str):
    """Bẫy lỗi ngày tháng không hợp lệ và trả về kết quả an toàn."""
    try:
        # Nếu hợp lệ, trả về đối tượng datetime
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        # Nếu ngày tháng sai logic (như 31/06), trả về None để báo lỗi
        return None