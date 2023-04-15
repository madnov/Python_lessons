def fibonachi_list():
    number = int(input('Введите число: '))
    fibonachi = []
    fib1, fib2 = 1, 0
    for i in range(number):
        fibonachi.append(fib2)
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
    print(fibonachi)


fibonachi_list()
