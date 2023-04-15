
def factorial():
    number = int(input('Введите число: '))
    result = 1
    factorials = []
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            result *= j
        factorials.append(result)
        result = 1
    return factorials


print(factorial())
