a = [2, 9, 7, 6, 3, 8, 5, 10]
def f(data:list):
    b = []  
    for i in data:
        if i % 2 == 0:
            b.append(i**2)
    return b
print(f(a))
    