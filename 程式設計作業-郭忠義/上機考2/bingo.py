def count(m, n):
    line = 0
    for i in range(n):
        #直線
        if all(m[i*n+j]for j in range(n)):
            line += 1
        if all(m[j*n+i]for j in range(n)):
            line += 1
    if all(m[i*n+i]for i in range(n)):
        line += 1
    if all(m[i*n+(n - i - 1)]for i in range(n)):
        line += 1
    return line
#input
p_n = int(input())
n = int(input())
number = input()
name = input().split()
num_s = []
for i in range(0, p_n):
    math = input().split()
    num_s.append(math)
circle = input().split()

for i in num_s:
    for j in range(len(i)):
        if i[j] not in circle:
            i[j] = 0
        else:
            i[j] = 1
answer = []

#output
for i in num_s:
    answer.append(count(i, n))
    
max_score = max(answer)
if len(set(answer)) == 1:
    print("Tie " + " ".join(name) +" " +  str(answer[0]))
else:
    for i in range(len(answer)):
        if answer[i] == max_score:
            print(name[i], end=" ")
    print(max_score)
