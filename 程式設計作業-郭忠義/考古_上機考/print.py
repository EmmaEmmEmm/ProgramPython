def func(t, n):
    #類型一
    if t == 1:
        for i in range(1, n + 1):
            print(str(i) * i + '#' * (n - i))
    #類型二
    elif t == 2:
        strd = str(1)
        for i in range(1, n + 1):
            print('#' * 2 * (n - i) + strd + strd[::-1].replace(strd[-1], ""))
            strd = strd + str(i + 1) 
    #類型三
    elif t == 3:
        strd = str(1)
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print('^' * (n - i))
        for i in range(1, n + 1):
            for j in range(n - i + 1 , 0, -1):
                print(j, end="")
            print('^' * (i - 1))
    #類型四
    elif t == 4:
        strd = str(1)
        for i in range(1, n + 1):
            print("^" * (n - i) + strd + strd[::-1].replace('1', '') + "^" * (n - i))
            strd = str(i+1) + strd
        strd = strd.replace(strd[0], "")
        for i in range(1, n):
            strd = strd.replace(strd[0], "")
            print("^" * i + strd + strd[::-1].replace('1', '')+ "^" * i)
def main():
    #輸入類型
    t = int(input())
    n = int(input())
    func(t, n)

main()