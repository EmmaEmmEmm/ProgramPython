a = input()
list = a.split()
b = []
for i in range(len(list)):
    if i == len(list) - 1:
        break
    else:
        b.append(int(list[i]) + int(list[i + 1]))              
print(b)