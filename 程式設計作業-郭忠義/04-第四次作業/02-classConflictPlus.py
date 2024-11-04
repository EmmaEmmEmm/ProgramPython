classNum = int(input())
classNumArray = []
timeArray = []
hours = []
change = 0

notclass=['61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c']
# input
for i in range(0, classNum):
    className = input()

    classNumArray.append(className)
    timeArray.append([])
    
    hour = int(input())
    hours.append(hour)
    for j in range(0, hour):
        time = input()
        timeArray[i].append(time)

for i in range(len(timeArray)):
    for k in range(len(timeArray[i])):
        for j in range(len(notclass)):
            if timeArray[i][k] == notclass[j]:
                print(-1)
                exit()
for i in range(len(hours)):
    if hours[i] < 1 or hours[i] > 3:
        print(-1)
        exit()

#output
if classNum < 2 or classNum > 10:
    print(-1)
else:
    level = len(classNumArray)
    for i in range(0, level):
        for k in range(i + 1, level):
            for j in range(0, len(timeArray[i])):
                for l in range(0, len(timeArray[k])):
                    if timeArray[i][j] == timeArray[k][l]:
                        change += 1
                        print('%s,%s,%s'%(classNumArray[i], classNumArray[k], timeArray[i][j]))
    if change == 0:
        print('correct')