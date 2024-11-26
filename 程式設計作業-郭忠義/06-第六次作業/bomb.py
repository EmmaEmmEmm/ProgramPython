n = int(input())
a = []
last = []
test = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(0, n):
    a.append(input().split())
    last.append([])


for i in range(0, n):
    for j in range(0, n):
        last[i].append(0)
        if a[i][j] == '1':
            last[i][j] == 0
        else:
            count = 0
            for x, y in test:
                ni, nj = i + x, j + y

                if 0 <= ni < n and 0 <= nj < n and a[ni][nj] == '1':
                    count += 1
            last[i][j] = count

for i in range(0, n):
    for j in range(0, n):
        print("%d "%last[i][j], end="")
    print()
        
