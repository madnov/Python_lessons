def count(func):
    def decorator(var):
        count = int(input('Введите количество: '))
        for _ in range(count):
            func(var)
    return decorator


@count
def main(var):
    request = int(input('Введите число: '))
    print(var * request)


main(10)
