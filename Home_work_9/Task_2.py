import numpy as np
# Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.


def identical_rows():
    matrix = np.random.randint(0, 2, (5, 5))
    print(matrix)
    if len(matrix) != len(set(map(tuple, matrix))):
        print("В массиве есть одинаковые строки")
    else:
        print("В массиве нет одинаковых строк")


identical_rows()
