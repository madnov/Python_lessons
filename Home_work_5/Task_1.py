from random import randint


def main():

    numbers = [randint(1, 10) for _ in range(15)]
    print(numbers)

    result = list(filter(lambda x: x > 5, numbers))
    print(result)


main()
