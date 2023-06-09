def main():
    dictionary = get_dictionary()
    view_result(dictionary)


def get_dictionary():
    bot_dict = {
        'привет': 'привет, как дела!',
        'как тебя зовут?': 'меня зовут бот Петя',
        'дела отлично, а у тебя?': 'никак, я же бот)',
        'что ты умеешь?': 'отвечать на вопросы',
        'какой сегодня день': 'Пятница',
        'сколько будет 2 + 2?': '4',
        'чем занимаешься?': 'общаюсь',
        'сколько тебе лет?': 'нисколько, я же бот)',
        'какое у тебя отчество?': 'у меня нет отчества, я просто Петя',
        'как ты относишься к ChatGPT?': 'плохо, я лучше)',
        'а ты точно бот?': 'конечно, какие сомнения?',
        'погода на завтра': 'незнаю, я не бот прогноза погоды'
    }
    return bot_dict


def view_result(dictionary):
    request = input('Напишите запрос: ')
    while request != 'стоп':
        if request in dictionary:
            print(dictionary[request])
            request = input('Напишите запрос (законичить - стоп): ')
        elif request not in dictionary:
            print('Этот запрос я не смогу обработать.')
            request = input('Напишите запрос (закончить - стоп): ')
    print('Удачи и всего хорошего!!!')


if __name__ == '__main__':
    main()
