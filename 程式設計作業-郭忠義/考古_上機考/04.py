def conflict(cl, d):
    for i in range(0, len(cl)):
        for j in range(i+1, len(cl)):
            for x in range(0, len(d[i])):
                for y in range(0, len(d[j])):
                    if d[i][x] == d[j][y]:
                        print(str(cl[i]) +" and " + str(cl[j]) + " conflict on " + str(d[i][x]))
def main():
    classroom = []
    time = []
    for i in range(0, int(input())):
        time.append([])
        classroom.append(int(input()))
        h = int(input())
        for j in range(0, h):
            time[i].append(int(input()))
    conflict(classroom, time)
main()