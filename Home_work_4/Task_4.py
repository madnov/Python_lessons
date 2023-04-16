def polynomial():
    # x = int(input('Введите значение x: '))
    with open('file_1.txt', 'r', encoding='utf-8') as f:
        product_1 = f.readline().split()
    with open('file_2.txt', 'r', encoding='utf-8') as f:
        product_2 = f.readline().split()
    result = product_1.copy()
    result[0][0] = int(product_1[0][0]) + int(product_2[0][0])
    print(result)

    # print(eval('{}{}'.format(product_1[0], product_1[1])))

    # print(type(product_1[0][0]))

# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8
polynomial()
