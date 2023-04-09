# Задача 3
quarter = int(input('Введите номер четверти: '))
while quarter < 1 or quarter > 4:
    print('Такой четверти нет')
    quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print('x > 0 , y > 0')
if quarter == 2:
    print('x < 0 , y > 0')
if quarter == 3:
    print('x < 0 , y < 0')
if quarter == 4:
    print('x > 0 , y < 0')