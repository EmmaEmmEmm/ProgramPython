totalClass = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
isChange = 0
for i in range(0, 3):
    for j in range(0, 3):
        totalClass[i][j] = int(input())
# 排序班級
totalClass.sort(key=lambda x:x[0])
# 排序課程
for i in range(0, 3):
    if totalClass[i][1] > totalClass[i][2]:
        a = totalClass[i][1]
        totalClass[i][1] = totalClass[i][2]
        totalClass[i][2] = a

for i in range(1, 3):
    for j in range(1, 3):
        if totalClass[0][i] == totalClass[1][j]:
            print('%d and %d conflict on %d'%(totalClass[0][0], totalClass[1][0],totalClass[1][j]))
            isChange += 1
            
for i in range(1, 3):
    for j in range(1, 3):
        if totalClass[0][i] == totalClass[2][j]:
            print('%d and %d conflict on %d'%(totalClass[0][0], totalClass[2][0],totalClass[2][j]))
            isChange += 1

for i in range(1, 3):
    for j in range(1, 3):
        if totalClass[1][i] == totalClass[2][j]:
                print('%d and %d conflict on %d'%(totalClass[1][0], totalClass[2][0],totalClass[1][i]))
                isChange += 1
if isChange == 0:
    print('correct')