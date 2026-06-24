import random
import string as str_lib

def generate_assignment_code():
    chars = str_lib.ascii_uppercase + str_lib.digits
    code = ''.join(random.choices(chars, k=4))
    print("--- SINH MÃ BÀI TẬP ---")
    print(f"Mã bài tập của bạn là: PY-{code}")