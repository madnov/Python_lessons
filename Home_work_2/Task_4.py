def main():
    numbers = create_numbers()
    print()
    print('Список со сдвигом')
    print(shift_array(numbers))


def create_numbers():
    numbers = []
    digit = int(input('Введите число: '))
    for i in range(-digit, digit + 1):
        numbers.append(i)
    print('Начальный список')
    print(numbers)
    return numbers


def shift_array(numbers):
    for j in range(2):
        for i in range(len(numbers) - 1, 0, -1):
            temp = numbers[i]
            numbers[i] = numbers[i - 1]
            numbers[i - 1] = temp
    return numbers


if __name__ == '__main__':
    main()
