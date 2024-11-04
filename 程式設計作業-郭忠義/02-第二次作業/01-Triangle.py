a = int(input())
b = int(input())
c = int(input())

high = [a, b, c]
high.sort(reverse=True)

max = high[0]
min1 = high[1]
min2 = high[2]

if min1 + min2 < max:
    print('Not Triangle')
else:
    if min1 == max and min2 == max:
        print('Equilateral Triangle')
        print('Isosceles Triangle')
        print('Acute Triangle')
    else:
        if min1 == max or min2 == max or min1 == min2:
            print('Isosceles Triangle')
            if max**2 > min1**2 + min2**2:
                print('Obtuse Triangle')
            elif max**2 < min1**2 + min2**2:
                print('Acute Triangle')
            else:
                print('Right Triangle')
        else:
            if max**2 > min1**2 + min2**2:
                print('Obtuse Triangle')
            elif max**2 < min1**2 + min2**2:
                print('Acute Triangle')
            else:
                print('Right Triangle')

            
