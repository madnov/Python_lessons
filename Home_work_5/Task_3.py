from random import randint


def main():
    numbers = get_numbers()
    numbers_2 = set(numbers)
    count = len(numbers) - len(numbers_2)
    print(numbers)
    print(f'{count} элемента совпадают')
    print('Список уникальных элементов:')
    print(list(numbers_2))


def get_numbers():
    return [randint(1, 10) for _ in range(10)]


if __name__ == '__main__':
    main()
