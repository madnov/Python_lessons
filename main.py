import numpy as np

# def task2():
#     size = 10
#     numbers = np.random.randint(10, 100, size)
#     print(numbers)

#     mean = np.mean(numbers)
#     print(f'среднее арифметическое {mean}')

    
#     num = int(input('\nВведите число: '))
#     dist = [np.abs(el - num) for el in numbers]
#     print(dist.index(min(dist)))
    
# task2()

def task4():
    matrix = np.random.randint(0, 100, (5, 5))
    print(matrix)
    diagonal = np.diagonal(matrix)
    print(diagonal)
    # print(result)
task4()
