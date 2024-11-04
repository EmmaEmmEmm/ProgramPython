score = []
total = 0
a = int(input())
if a == 10:
    score.append(a)
    a = int(input())
    if a == 10:
        score.append(a)
    else:
        score.append(a)
        a = int(input())
        score.append(a)
else:
    score.append(a)
    a = int(input())
    score.append(a)
    a = int(input())
    if a == 10:
        score.append(a)
    else:
        score.append(a)
        a = int(input())
        score.append(a)
for i in range(0, 2):
    a = int(input())
    score.append(a)
    if a == 10:
        for i in range(0, 2):
            a = int(input())
            score.append(a)
        break
if score[-1] + score[-2] == 10:
    a = int(input())
    score.append(a)

for i in range(0, len(score)):
    total += score[i]

if score[0] == 10:
    total += score[1] + score[2]
    if score[1] + score[2] == 10:
        total += score[3]
    elif score[1] == 10:
        total+= score[2] + score[3]
elif score[0] + score[1] == 10:
    total += score[2]
    if score[2] + score[3] == 10:
        total += score[4]
else:
    if score[2] + score[3] == 10:
        total += score[4]
print(total)