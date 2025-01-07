n = int(input())
m = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
circle = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if a[i*n+j] not in circle:
            a[i*n+j] = 0
        if b[i*n+j] not in circle:
            b[i*n+j] = 0

def fin(lis):
    line = 0
    for i in range(n):
        if all(lis[i*n+j] for j in range(n)):
            line = line + 1
        if all(lis[j*n+i] for j in range(n)):
            line = line + 1
    if all(lis[i*n+i] for i in range(n)):
        line = line + 1
    if all(lis[i*n+(n - i - 1)] for i in range(n)):
        line = line+1
    return line

a = fin(a)
b = fin(b)
if a > b:
    print("A win")
elif a == b:
    print("Tie")
else:
    print("B win")