x = [5, 8, 1, 2, 6, 4 ,6]
def f(a:list):
    b = 0
    for i in range(0, len(a)):
        if a[len(a) - 1] < a[i]:
            b = a[len(a) - 1]
            a[len(a) - 1] = a[i]
            a[i] = b
    a.pop()
    for i in range(0, len(a)):
        if a[len(a) - 1] < a[i]:
            b = a[len(a) - 1]
            a[len(a) - 1] = a[i]
            a[i] = b
    return a[len(a) - 1]
print(f(x))