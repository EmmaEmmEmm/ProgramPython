n = int(input())
for i in range(0, n):
    for j in range(0, n - i):
        print(2*(n - j - 1) + 1, end="")
    print("$" * (i), end="")
    print()