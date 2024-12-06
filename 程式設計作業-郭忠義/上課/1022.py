a = list(map(int, input().split()))
b = int(input())
a = sorted(a)
liste = set()
def f(n=0, string=""):
    if n == b:
        liste.add(tuple(sorted(string)))
        return
    for i in a:
        if not str(i) in string:
            if n + i <= b:
                f(n + i, string + str(i))
f()
result = [list(c) for c in liste]
print(result)