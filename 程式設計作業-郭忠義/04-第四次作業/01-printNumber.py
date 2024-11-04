n = int(input())
def f(n, mark):
    for i in range(0, n):
        print(mark, end='')
def Nnumber(n):
    for i in range(n - 2, -1, -1):
        print(2 * i + 1, end='')
def number(n):
    for i in range(0, n):
        print(2 * i + 1, end='')
for j in range(0, n - 1):
    f(n - j - 1, '*')
    number(j + 1)
    Nnumber(j + 1)
    print()
for j in range(0, n):
    f(j, '*')
    number(n - j)
    Nnumber(n - j)
    print()
if n <= 0:
    print("Error")