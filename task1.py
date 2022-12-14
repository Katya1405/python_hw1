# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Enter the number of the day of the week: '))
col = range(1, 8)
if day in col:
    if day == col[5] or day == col[6]:
        print('This day is the holiday')
    else:
        print('This day is the workday')
else:
    print('Incorrect value')
