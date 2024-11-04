n = int(input())
m = int(input())
c = int(input())

if c == 1:
    if m % 2 == 1:
        for i in range(0, n):
            print("_" * (n - i - 1) + "*" * (2 * i + 1) + "_" * (2 * (n - i - 1)) + "*" * (i + 1))
        for i in range(1, n):
            print("_" * (i) + "*" * (2 *(n - i - 1) + 1) + "_" * (2 * (i)) + "*" * (n - i))
    else:
        for i in range(0, n):
            print("*" * (i + 1) +  "_" * (2 * (n - i - 1)) + "*" * (2 * i + 1) + "_" * (n - i - 1))
        for i in range(1, n):
            print("*" * (n - i) + "_" * (2 * (i)) + "*" * (2 *(n - i - 1) + 1) + "_" * (i))
else:
    if m % 2 == 0:
        for i in range(0, n):
            strtext = ""
            for j in range(n - i, 0, -1):
                strtext += str(j)
            print("_" * i + strtext + strtext[::-1].replace("1", "") + "_" * i, end="")
            print()
    else:
        for i in range(n - 1, -1, -1):
            strtext = ""
            for j in range(n - i, 0, -1):
                strtext += str(j)
            print("_" * i + strtext + strtext[::-1].replace("1", "") + "_" * i , end="")
            print() 
    