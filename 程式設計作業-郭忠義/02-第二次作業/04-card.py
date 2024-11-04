def getData():
    x = [input(), input(), input(), input(), input(), input()]
    return x
def compute():
    totalx = 0
    totaly = 0
    x = getData()

    for i in range (0, 6):
        if x[i] == 'J' or x[i] == 'Q' or x[i] == 'K':
            if i > 2:
                totaly += 0.5
            else:
                totalx += 0.5
        elif x[i] == 'A':
            if i > 2:
                totaly += 1
            else:
                totalx += 1
        else:
            if i > 2:
                totaly += int(x[i])
            else:
                totalx += int(x[i])
    if totalx > 10.5:
        totalx = 0
    if totaly > 10.5:
        totaly = 0
    total = [totalx, totaly]
    return total

def printAnswer():
    total = compute()   
    if total[0] % 1.0 == 0:
        print(int(total[0]))
    else:
        print(total[0])

    if total[1] % 1.0 == 0:
        print(int(total[1]))
    else:
        print(total[1])

    if total[1] > total[0]:
        print('Y Win')
    elif total[1] < total[0]:
        print('X Win')
    else:
        print('Tie')
    
printAnswer()