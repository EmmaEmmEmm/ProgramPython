ans_list = []
AB = input()

def create_ans(string=""):
    if len(string) == 5:
        ans_list.append(string)
        return
    for i in range(10):
        if not str(i) in string:
            create_ans(string + str(i))

def check(check, ans):
    a, b = 0, 0
    for i in range(len(check)):
        if check[i] in ans:
            if i == ans.index(check[i]): a += 1
            else: b += 1
    return f"{a}A{b}B"
    
create_ans()
while True:
    print(AB)
    check_str = ans_list[0]
    B = check(check_str, AB)
    if check_str == AB:
        print(check_str)
        break
    current_ans_list = []
    for i in ans_list:
        if B == check(check_str, i):
            current_ans_list.append(i)

    ans_list = current_ans_list