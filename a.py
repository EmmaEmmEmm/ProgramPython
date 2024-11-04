lineOne = input().split()
lineTwo = input().split()

num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
color = ['S', 'H', 'D', 'C']
test = []
for i in range(0, len(num)):
    for j in range(0, len(color)):
        test.append(num[i] + color[j])

def error(a):
    for i in a:
        if i not in test:
            return 1
print(error(lineOne))
print(error(lineTwo))
