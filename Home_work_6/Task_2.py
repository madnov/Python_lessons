from random import randint


def main():
    number = get_number()
    numbers = [randint(1, 9) for _ in range(15)]
    result = get_result(number, numbers)
    print(numbers)
    print(result)


def get_number():
    number = int(input('Введите трёхзначное число: '))
    while number < 100 or number > 999:
        number = int(input('Введите трёхзначное число: '))
    return number


def get_result(number, numbers):
    num = list(str(number))
    length = len(num)
    num = [int(i) for i in num]
    for i in range(len(numbers)):
        if num == numbers[i:length + i]:
            return 'Yes'
    return 'No'    

if __name__ == '__main__':
    main()
