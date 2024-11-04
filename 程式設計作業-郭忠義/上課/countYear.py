def AmazingCount(num, year):
    result = (((num*2)+5)*50) + 1774 - year
    phone = result//100
    age = result%100
    a = [phone, age]
    return a

num = int(input())
year = int(input())

result = AmazingCount(num,year)
print('phoneNumber:%d, Age:%d'%(result[0], result[1]))