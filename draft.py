

def mini_game():
    from random import randint
    computer_number = randint(1, 1000)
    user_number = int(input('Угадайте число от 1 до 1000: '))
    count = 0
    while user_number != computer_number:
        if computer_number > user_number:
            count += 1
            print('Загаданное число больше, попробуйте ещё раз.')
            user_number = int(input('Угадайте число от 1 до 1000: '))
        elif computer_number < user_number:
            count += 1
            print('Загаданное число меньше, попробуйте ещё раз.')
            user_number = int(input('Угадайте число от 1 до 1000: '))
    print(
        f"Поздравляем вы угадали c {count} попытки, загаданное число: {computer_number} ")


mini_game()
