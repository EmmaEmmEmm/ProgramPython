pl1 = input().split()
pl2 = input().split()
computer = input().split()

refuse = []

def re(n, l):
    if n < 0:
        return l
    else:
        length = len(l)
        for i in range(n-1, -1, -1):
            if l[n][1] == l[i][1]:
                refuse.append(l[n])
                refuse.append(l[i])
                l.remove(l[n])
                l.remove(l[i])
                break
        if length > len(l):
            return re(n - 2, l)
        else:
            return re(n - 1, l)
def f(s, l, l2):
    if s in refuse:
        return 1
    elif s in l2:
        l2.remove(s)
        l.append(s)
        return re(len(l)-1, l)
    else:
        return 1

re(len(pl1)-1, pl1)
re(len(pl2)-2, pl2)
re(len(computer)-1, computer)
pl = f(input(), re(len(pl1)-1, pl1), pl2)
pl2 = f(input(), re(len(pl2)-1, pl2), computer)
c = f(input(), re(len(computer)-1, computer), pl1)

if pl == 1 or pl2 == 1 or c == 1:
    print("Error")
else:
    print(" ".join(pl1))
    print(" ".join(pl2))
    print(" ".join(c))