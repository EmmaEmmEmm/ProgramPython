n = int(input())
def f(n, mark):
    for i in range(n):
        print(mark, end='')
def Nnumber(n):
    for i in range(n, 0, -1):
        print(2 * i + 1, end='')
def number(n):
    for i in range(n):
        print(2 * i + 1, end='')
for j in range(0, n + 1):
    f(n - j, '#')
    Nnumber(j)
    number(j + 1)
    print()