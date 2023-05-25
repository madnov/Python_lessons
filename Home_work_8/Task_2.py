# Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

import telebot


bot = telebot.TeleBot('')

@bot.message_handler(commands=['ответ'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     f'Здравствуйте {message.from_user.first_name} ')

@bot.message_handler(content_types=['text'])
def request(message):
    text = message.text
    if text != 'ok':
        with open('appel.txt', 'r', encoding='utf-8') as file:
            request = file.read().replace('\n', ':').split(':')    
        answer = 'Погода завтра будет солнечная'
        bot.send_message(request[0], f'Вы спрашивали: {request[1]}')
        bot.send_message(request[0], f'Ответ: {answer}')


bot.polling()
