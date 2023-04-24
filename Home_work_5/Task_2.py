from random import randint


def main():
    numbers = [randint(1, 20) for _ in range(10)]
    print(numbers)
    result = []
    temp = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > temp[-1]:
            temp.append(numbers[i])
        else:
            if len(temp) > len(result):
                result = temp
            temp = [numbers[i]]

    if len(temp) > len(result):
        result = temp
    print(result)


main()
