ans_list = []
def create(string=""):
    if len(string) == 4:
        ans_list.append(string)
        return
    for i in range(10):
        if str(i) not in string:
            create(string + str(i))

def check(check, ans):
    a, b = 0, 0
    for i in range(len(check)):
        if check[i] in ans:
            if check[i] == ans[i]:
                a += 1
            else:
                b += 1
    return f"{a}A{b}B"
create()

while 1:
    check_str = ans_list[0]
    AB = input(ans_list[0] + "\n")
    if AB == "1":
        break
    current_list = []

    for i in ans_list:
        if AB == check(check_str, i):
            current_list.append(i)
    ans_list = current_list