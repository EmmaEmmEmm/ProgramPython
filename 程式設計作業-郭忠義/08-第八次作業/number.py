list1 = []
for _ in range(4):
    a = input().split()
    list1.append(a)
w, x, y, z = 0
for i in range(2):
    for j in range(2):
        if list[i][j] == 0:w+=1
        if list[i][j+2] == 0:x+=1
        if list[i+2][j] == 0:y+=1
        if list [i+2][j+2] == 0:z+=1

