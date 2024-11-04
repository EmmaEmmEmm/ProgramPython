card = str(input())
cards = card.split()
#error input
def check(l):
    a = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K'}
    b = {'S', 'H', 'D', 'C'}
    c = 0
    for i in l:
        if len(i) != 2:
            if i[1] == '0':
                c = c + 0
            else:
                c = c + 1
        else:
            if i[0] not in a:
                c = c + 1
            if i[1] not in b:
                c = c + 1
    if c >= 1:
        return 1
    else:
        return 0
def D(l):
    l = set(l)
    if len(l) < 5:
        return 1
    else: 
        return 0
def num(l):
    num = []
    num_count = []
    s = []
    
    for i in l:
        if i[0] == '1' and i[1] == "0":
            num.append(10)
        elif i[0] == 'A':
            num.append(1)
        elif i[0] == 'J':
            num.append(11)
        elif i[0] == 'K':
            num.append(13)
        elif i[0] == 'Q':
            num.append(12)
        else:
            num.append(int(i[0]))
            
    num_c = list(set(num))
    num_c = sorted(num_c)
    for i in set(num_c):
        s.append(i)
        if i + 1 not in num_c:
            break
    if len(s) == 5 or num_c == [1, 2, 3, 4, 13] or num_c == [1, 2, 3, 12, 13] or num_c == [1, 2, 11, 12, 13] or num_c == [1, 10, 11, 12, 13]:
        return 1
    else:
        for i in range(len(num_c)):
            num_count.append(0)
            for j in num:
                if num_c[i] == j:
                    num_count[i] += 1
        
        num_count = sorted(num_count, reverse=True)
        return num_count  
def color(l):
    color = []  
    color_count = []

    for i in l:
        if i[1] == '0':
            color.append(i[2])
        else:
            color.append(i[1])

    color_c = list(set(color))

    for i in range(len(color_c)):
        color_count.append(0)
        for j in color:
            if color_c[i] == j:
                color_count[i] += 1
    color_count = sorted(color_count, reverse=False)
    return color_count
 
if check(cards):
    print('Error input')
elif D(cards):
    print('Duplicate deal')
elif num(cards) == 1 and color(cards) == [5]:
    print(9)
elif num(cards) == [4, 1]:
    print(8)
elif num(cards) == [3, 2]:
    print(7)
elif color(cards) == [5]:
    print(6)
elif num(cards) == 1:
    print(5)
elif num(cards) == [3, 1, 1]:
    print(4)
elif num(cards) == [2, 2, 1]:
    print(3)
elif num(cards) == [2, 1, 1, 1]:
    print(2)
else:
    print(1)