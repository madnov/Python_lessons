import numpy as np
# Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.


def matrix_indexes():
    matrix = np.random.randint(
        1, 100, (np.random.randint(1, 20), np.random.randint(1, 20)))
    print(matrix)
    print()
    max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
    min_index = np.unravel_index(np.argmin(matrix), matrix.shape)
    print("Индекс максимального элемента:", max_index)
    print("Индекс минимального элемента:", min_index)


def matrix_diagonal():
    matrix = np.random.randint(1, 100, (5, 5))
    result = np.diagonal(matrix)
    print(f'Матрица:\n{matrix}')
    print()
    print(f'Диагональ матрицы:\n{result}')


matrix_indexes()
print()
matrix_diagonal()
