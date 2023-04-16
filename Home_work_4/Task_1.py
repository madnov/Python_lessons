def main():
    number = int(input('Введите число: '))
    simple_multiply = get_simple_multiply(number)
    print(f'Список простых чисел - {simple_multiply}')
    print(f'Количество простых чисел - {len(simple_multiply)}')


def get_simple_multiply(number):
    list_multiply = []
    
    for i in range(2, number):
        if number % i == 0:
            number //= i
            list_multiply.append(i)
            if number % i == 0:
                number //= i
                list_multiply.append(i)
            

    return list_multiply


if __name__ == '__main__':
    main()
