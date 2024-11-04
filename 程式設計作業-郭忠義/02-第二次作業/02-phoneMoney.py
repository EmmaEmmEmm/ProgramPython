import math
lineIn = int(input())
lineOut = int(input())
city = int(input())
messagerIn = int(input())
messagerOut = int(input())

sd = [183, 383, 983]
lineInArray = [0.08, 0.07, 0.06]
lineOutArray = [0.1393, 0.1304, 0.1087]
cityArray = [0.1349, 0.1217, 0.1018]
messagerInArray = [1.1287, 1.1127, 0.9572]
messagerOutArray = [1.4803, 1.2458, 1.1243]

total = [0, 0, 0]
for i in range (0, 3):
    total[i] = math.floor(lineIn*lineInArray[i]+lineOut*lineOutArray[i]+city*cityArray[i]+messagerIn*messagerInArray[i]+messagerOut*messagerOutArray[i])
    if i==2 or total[i]<sd[i+1]:
        if total[i]<sd[i]:
            print(sd[i])
        else:
            print(total[i])
        print(sd[i])
        break
