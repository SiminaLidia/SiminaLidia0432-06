x = int(input("произвольное число: "))
y = int(input("пограничное число: "))
if (x > y):
    print('{} больше {}'.format(x, y))
    if (x> 3 * y):
        print('{} больше {} более, чем в 3 раза'.format(x, y))
        if (x < y):
            print('{} меньше {}'.format(x, y))
