def turnRNine(a, n):
    a = a[::-1]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            else:
                a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

def asd(d, a, n):
    if d < -1 or d > 2:
        return ["ERROR"]
    elif d == 0:
        return a
    elif d == 1:
        return a[::-1]
    elif d == 2:
        return turnRNine(a, n)
def main():
    n = int(input())
    if n < 1 or n > 10:
        print("ERROR")
    else:
        b = []
        while 1:
            d = int(input())
            if d == -1:
                break
            else:
                ar = []
                for i in range(0, n):
                    ar.append([])
                    for j in range(0, n):
                        ar[i].append(i*n + j)
                ar = asd(d, ar, n)
                b.append(ar)
        for i in range(0, len(b)):
            for j in range(0, len(b[i])):
                if b[i][0] == "ERROR":
                    print("ERROR")
                else:
                    for k in range(0, len(b[i][j])):
                        print("%3d"%b[i][j][k], end="")
                print()
main()