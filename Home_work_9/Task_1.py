import numpy as np
# Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.


def uniq_numbers():

    array = np.random.randint(0, 100, (20))
    print(array)
    uniq = len(np.unique(array))
    print(f'Количество уникальных элементов в списке : {uniq}')



uniq_numbers()