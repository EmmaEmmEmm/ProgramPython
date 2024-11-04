def error(a):
    num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    color = ['S', 'H', 'D', 'C']

    test = []
    for i in num:
        for j in color:
            test.append(i + j)        

    for i in a:
        if i not in test:
            return 1
        
def d(a, b):
    for i in a:
        if i in b:
            return 1
        
def colorA(a):
    b = []
    for i in a:
        if i[0] == "1":
            b.append(i[2])
        else:
            b.append(i[1])
    b = list(set(b))
    if len(b) == 1:
        return 1
    else:
        return b
    
def numA(a):
    num = []
    count = []
    for i in a:
        if i[0] == '1':
            num.append(10)
        elif i[0] == 'A':
            num.append(1)
        elif i[0] == 'J':
            num.append(11)
        elif i[0] == 'Q':
            num.append(12)
        elif i[0] == 'K':
            num.append(13)
        else:
            num.append(int(i[0]))
    
    num_t = sorted(set(num))
    for i in num_t:
        count.append(i)
        if i + 1 not in num_t:
            break
    if len(count) == 5 or num_t == [1, 10, 11, 12, 13] or num_t == [1, 2, 11, 12, 13] or num_t == [1, 2, 3, 12, 13] or num_t == [1, 2, 3, 4, 13]:
        return 1
    else:
        number = []
        for i in range(0, len(num_t)):
            number.append(0)
            for j in num:
                if j == num_t[i]:
                    number[i] += 1
        return sorted(number, reverse=True)
    
def max(a):
    if numA(a) == 1 and colorA(a) == 1:
        return 9
    elif numA(a) == [4, 1]:
        return 8
    elif numA(a) == [3, 2]:
        return 7
    elif colorA(a) == 1:
        return 6
    elif numA(a) == 1:
        return 5
    elif numA(a) == [3, 1, 1]:
        return 4
    elif numA(a) == [2, 2, 1]:
        return 3
    elif numA(a) == [2, 1, 1, 1]:
        return 2
    else:
        return 1
    
def main():
    lineOne = input().split()
    lineTwo = input().split()
    if error(lineOne) == 1 or error(lineTwo) == 1:
        print("Error input")
    elif d(lineOne, lineTwo) == 1:
        print("Duplicate deal")
    else:
        one = max(lineOne)
        two = max(lineTwo)
        if one >= two:
            print(one)
        else:
            print(two)

main()