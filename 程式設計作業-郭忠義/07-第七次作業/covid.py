t = int(input())
m = int(input())
first = int(input())
total = 0

data = [float(input()), int(input()), float(input())]
l = [1, first, first, 0]
covid = []

def f(n, l, d, total):
    if n > m:
        return total
    else:
        covid.append(l[2])
        total += l[2]
        if n - d[1] >= 1:
            d[2] += covid[n-d[1]-1]/t
            l[1] -= covid[n-d[1]-1]
            l[3] = covid[n-d[1]-1]
        print(" ".join(map(str, l)))
        l = list(map(int, l))
        l[0] = n +1
        if int(l[1]) >= int(t*(1-d[2])):
            y = 0
        else:
            y = int(l[1]*(d[0]/d[1])*(1-d[2]))
        l[1] += y
        if l[1] > t*(1-d[2]):
            l[1] -= y
            l[2] = round(t*(1-d[2])) - l[1]
            l[1] = round(t*(1-d[2]))
        else:
            l[2] = y
        return f(l[0], l, d, total)
print(f(l[0], l, data, total))