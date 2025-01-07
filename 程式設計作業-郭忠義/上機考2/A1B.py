ans_list = []
def create(string=""):
    if len(string) == 5:
        ans_list.append(string)
        return
    for i in range(10):
        if str(i) not in string:
            create(string + str(i))
create()

def check(c, d):
    a, b = 0, 0
    for i in range(len(c)):
        if c[i] in d:
            if i == d.index(c[i]):a+=1
            else:b+=1
    return f"{a}A{b}B"

a = input()
while 1:
    current = ans_list[0]
    b = check(current, a)

    if b == "5A0B":
        print(ans_list[0])
        break
    else:
        current_list = []
        for i in ans_list:
            if b == check(current, i):
                current_list.append(i)
        ans_list = current_list