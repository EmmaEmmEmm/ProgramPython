ans_list = []

def create_ans(string=""):
    if len(string) == 5:
        ans_list.append(string)
        return
    for i in range(10):
        if str(i) not in string:
            create_ans(string + str(i))

def check(guess, answer):
    a, b = 0, 0
    for i in range(len(guess)):
        if guess[i] in answer:
            if i == answer.index(guess[i]):
                a += 1
            else:
                b += 1
    return f"{a}A{b}B"

create_ans()
AB = input().strip()

while True:
    check_str = ans_list[0]
    feedback = check(check_str, AB)
    
    if feedback == "5A0B":
        print(check_str)
        break

    current_ans_list = []
    for i in ans_list:
        if check(check_str, i) == feedback:
            current_ans_list.append(i)
    
    ans_list = current_ans_list

