# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

col = range(1, 5)
number = int(input('enter the quarter number: '))
if number in col:
    if number == 1:
        print('[x>0; y>0]')
    elif number == 2:
        print('[x<0; y>0]')
    elif number == 3:
        print('[x<0; y<0]')
    else:
        print('[x>0; y<0]')
else:
    print('-')
