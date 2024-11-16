def f(n):
    if n < 10:
        return n
    else:
        return f(n%10) + f(n//10)
def main():
    n = int(input())
    print(f(n))
main()