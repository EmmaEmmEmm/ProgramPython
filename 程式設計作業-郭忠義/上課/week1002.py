def f(n):
    d = n%10
    if n == 0:
        return 0
    else:
        n = n//10
        return f(n) + d
def main():
     n = int(input())
     print(f(n))
main()