def calculate_check_digit(id_number):
    """計算身份證字號檢查碼是否合法"""
    area_code_map = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
        'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
        'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33
    }
    if id_number[0] not in area_code_map:
        return "Wrong area code"
    if id_number[1] not in '12':
        return "Wrong gender code"

    area_code_value = area_code_map[id_number[0]]
    full_digits = f"{area_code_value}{id_number[1:]}"
    weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    total = sum(int(full_digits[i]) * weight[i] for i in range(10))
    remainder = total % 10
    check_digit = (10 - remainder) % 10
    return "Pass" if check_digit == int(id_number[-1]) else "Illegal"

def calculate_password_strength(password):
    """計算密碼強度"""
    import re

    lower_count = sum(1 for c in password if c.islower())
    upper_count = sum(1 for c in password if c.isupper())
    digit_count = sum(1 for c in password if c.isdigit())
    special_count = sum(1 for c in password if c in "~!@#$%^&*<>_+=")

    strength = lower_count + 3 * upper_count + 2 * digit_count + 5 * special_count

    # 檢查五個以上數字且位置不相鄰
    if digit_count >= 5:
        digits_positions = [i for i, c in enumerate(password) if c.isdigit()]
        if all(abs(digits_positions[i] - digits_positions[i - 1]) > 1 for i in range(1, len(digits_positions))):
            strength += 15

    return strength

def main():
    # 輸入
    id_number = input().strip()
    password = input().strip()

    # 驗證身份證字號
    id_check_result = calculate_check_digit(id_number)
    print(id_check_result)

    # 計算密碼強度
    password_strength = calculate_password_strength(password)
    if password_strength >= 30:
        print(password_strength)
    else:
        print(f"{password_strength} Not strong enough")

if __name__ == "__main__":
    main()
