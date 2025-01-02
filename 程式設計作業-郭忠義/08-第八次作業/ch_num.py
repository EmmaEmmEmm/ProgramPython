def is_valid_license_plate(s):
    # 定義禁用的字母碼和規則
    forbidden_letters = {"I", "O"}
    forbidden_combinations = {
        "FUC", "FUG", "FUQ", "FUT", "GPU", "KGB", "KKK", "KMT", "DPP",
        "PUG", "PUP", "CAT", "ANT", "APE", "MAD", "NUN", "SEX", "SLY",
        "BAD", "GAY", "ASS", "BUM", "BRA", "CRY"
    }

    # 驗證格式
    if not (len(s) == 8 and s[3] == '-' and s[:3].isalpha() and s[4:].isdigit()):
        return f"{s} is Invalid license plate number."

    # 驗證字母部分
    letters = s[:3]
    if any(c in forbidden_letters for c in letters) or letters in forbidden_combinations:
        return f"{s} is Invalid license plate number."

    # 驗證數字部分
    numbers = s[4:]
    if '4' in numbers:
        return f"{s} is Invalid license plate number."

    return f"{s} is Valid license plate number."

a = input()

print(is_valid_license_plate(a))