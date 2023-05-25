#Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot


bot = telebot.TeleBot('')

@bot.message_handler(commands=['техподдержка'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     f'Здравствуйте {message.from_user.first_name}, это бот техподдержки. ')

@bot.message_handler(content_types=['text'])
def request(message):
    text = message.text
    if text != '':
        with open('appel.txt', 'a', encoding='utf-8') as data:
            text = f'{message.from_user.id}: {message.text}\n'
            data.write(f'{text}')
        


bot.polling()
