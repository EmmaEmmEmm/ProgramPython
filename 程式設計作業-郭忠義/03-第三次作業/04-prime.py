a = input()
b = a.split()
primeList = []
def prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    if n != 1:
        primeList.append(n)   
for i in range(len(b)):
    prime(int(b[i]))
primeList.sort()
if len(primeList) == 0:
    print("No prime number")
else:
    print(primeList)
