num = input()
nums = num.split()
total = int(input())

setd = []
plus = []
a = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if int(nums[i]) + int(nums[j]) == total:
            setd.append([i, j])
for i in range(len(setd)):
    if i >= 1:
        if int(setd[i][0]) * int(setd[i][1]) > int(setd[i - 1][0]) * int(setd[i - 1][1]):
            a = i
        else:
            a = 0
setd[a] = sorted(setd[a], reverse=True)
print(setd[a])


