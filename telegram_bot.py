import telebot
import requests
from telebot import types
from random import randint

bot = telebot.TeleBot('')

markup = types.ReplyKeyboardMarkup(row_width=1)
btm_reg = types.KeyboardButton('регистрация')
btm_alarm = types.KeyboardButton('оповещение')
markup.add(btm_reg, btm_alarm)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     "Привет, я бот Питоша.", reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def greetings(message):
#     # print(message)
#     text = message.text
#     if 'привет' in message.text:
#         bot.reply_to(message, f'Привет, {message.from_user.first_name}')
#     elif text.lower() == 'погода':
#         req = requests.get('https://wttr.in/?0T')
#         bot.reply_to(message, req.text)
#     elif text.lower() == 'котик':
#         req = requests.get('https://cataas.com/cat')
#         bot.send_photo(message.from_user.id, req.content)

@bot.message_handler(content_types=['text'])
def text_message(message):
    with open('log.txt', 'a', encoding='utf-8') as data:
        text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
        data.writelines(text)

    if message.text.lower() == 'регистрация':
        with open('registred_users.txt', 'r', encoding='utf-8') as data:
            id_list = data.readlines()
            id_list = list(el[:-1] for el in id_list)
        if str(message.from_user.id) not in id_list:
            with open('registred_users.txt', 'a', encoding='utf-8') as data:
                data.write(f'{message.from_user.id}\n')
                bot.reply_to(message, 'Регистрация прошла успешно!')
        else:
            bot.reply_to(message, 'Вы уже зарегистрированы!')

    elif message.text.lower() == 'оповещение':
        with open('registred_users.txt', 'r', encoding='utf-8') as data:
            id_list = data.read().split('\n')
            id_list = id_list[:-1]
        for id in id_list:
            if id != '':
                bot.send_message(id, 'совещание через 5 минут')


# @bot.message_handler(content_types=['text'])
# def mini_game(message):
#     text = message.text
#     count = 0
#     comp_number = randint(1, 1000)
#     if text.lower() == 'игра':
#         us_number = bot.reply_to(message, 'Угадайте число от 1 до 1000: ')
#         if us_number != comp_number:
#             if us_number > comp_number:
#                 count += 1
#                 us_number = bot.reply_to(message, 'Загаданное число больше, попробуйте ещё раз')
#             elif us_number < comp_number:
#                 us_number = bot.reply_to(message, 'Загаданное число меньше, попробуйте ещё раз')
#                 count += 1
bot.polling()
