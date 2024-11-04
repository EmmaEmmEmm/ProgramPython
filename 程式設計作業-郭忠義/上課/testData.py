temperature = int(input())
wind = int(input())
humidity = int(input())

if temperature >= 30 and wind == 0:
    print('開冷氣')
elif humidity >= 85:
    print('開除濕')
else:
    print('關冷氣')

