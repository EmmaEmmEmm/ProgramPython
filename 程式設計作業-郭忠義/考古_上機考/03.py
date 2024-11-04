def turnLNine(a, n):
    for i in range(0, n):
        for j in range(i, n):
            if i == j:
                continue
            else:
                a[i][j], a[j][i] = a[j][i], a[i][j]
    return a[::-1]
def turnRNine(a, n):
    a = a[::-1]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            else:
                a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
def RLturn(a):
    for i in range(0, len(a)):
        a[i] = a[i][::-1]
    return a
def asd(d, a, n):
    if d == 1:
        return turnLNine(a, n)
    elif d == 2:
        return turnRNine(a, n)
    elif d == 3:
        return a[::-1]
    else:
        return RLturn(a)
def main():
    n = int(input())
    d = int(input())
    ar = []
    for i in range(0, n):
        ar.append([])
        for j in range(1, n+1):
            ar[i].append(i*n + j)
    ar = asd(d, ar, n)
    for i in range(len(ar)):
        for j in range(len(ar)):
            print("%3d"%(ar[i][j]), end="")
        print()
main()