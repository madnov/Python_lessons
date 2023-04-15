
def find_count():
    count = 0
    substring = input('Введите первую строку: ')
    string = input('Введите вторую строку: ')
    for i in substring:
        for j in string:
            if i == j:
                count += 1
        print(f'{i} - {count}\t', end=' ')
        count = 0


find_count()
