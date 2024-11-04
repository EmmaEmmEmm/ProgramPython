n = eval(input())
if n % 2 == 0:
    for i in range(0, n):
        if i == 0 or i == n - 1:
            for j in range(0, n):
                print('*', end='')
        else:
            for k in range(0, n):
                if k == 0 or k == n - 1:
                    print('*', end='')
                else:
                    print('#', end='')
        print()
else:
    for i in range(0,n):                
        for j in range(n-i,1,-1):
            print('#',end='')
        for k in range(0,i * 2 + 1,1):
            print('*',end='')
        print()

    