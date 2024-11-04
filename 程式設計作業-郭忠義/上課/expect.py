def my_divide(a:int, b:int):
    try:
        c = a / b
        print('c=', c)
    except ZeroDivisionError:
        print('divided 0!!!')
    except ValueError:
        print('value')
    else:
        print('no error')
    finally:
        print('always')

my_divide(10, 0)
my_divide(1, 1)
my_divide('a', 4)