def f(n):
    if n == 0 or n == 1:
        return 0
    elif n % 2 == 0:
        return f(n/2) + 1
    else:
        return f((n+1)/2) + 1
list1 = []
while 1:
    b = input()
    a = int(b, 2)
    if b == "-1":
        break
    list1.append(a)

for i in list1:
    d = bin(f(i))
    if len(d) == 6:
        print(d.replace("0b", ""))
    elif len(d) == 5:
        print(d.replace("0b", "0"))
    elif len(d) == 4:
        print(d.replace("0b", "00"))
    else:
        print(d.replace("0b", "000"))
