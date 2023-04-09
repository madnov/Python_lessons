# Задача 2
from math import sqrt
x1 = int(input('Введите первую координату точки A: '))
y1 = int(input('Введите вторую координату точки A: '))
x2 = int(input('Введите первую координату точки B: '))
y2 = int(input('Введите вторую координату точки B: '))
result = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'{result:.2f}')