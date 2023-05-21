from random import randint
import telebot


bot = telebot.TeleBot('')
comp_number = randint(1, 1000)
count = 1
count += 1


@bot.message_handler(commands=['игра'])
def send_welcome(message):
    bot.reply_to(
        message, 'Давай поиграем в игру "угадай число": Введите число от 1 до 1000')


@bot.message_handler(content_types=['text', comp_number])
def mini_game(message):
    us_number = int(message.text)
    if us_number != comp_number:
        if us_number < comp_number:
            us_number = bot.reply_to(
                message, 'Загаданное число больше, попробуйте ещё раз')
        elif us_number > comp_number:
            us_number = bot.reply_to(
                message, 'Загаданное число меньше, попробуйте ещё раз')
    elif us_number == comp_number:
        bot.reply_to(message, f'Поздравляем!!!! Вы угадали с {count} попытки')
        


bot.polling()
