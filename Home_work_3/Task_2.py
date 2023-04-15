def main():
    fruit = get_fruit_list()
    request = get_request()
    result = get_result(fruit, request)
    if bool(result) == False:
        print('Такого фрукта не существует.')
    else:
        print(*result)
    

def get_fruit_list():
    fruit_list = [
                  'абрикос', 'авокадо', 'апельсин', 'айва', 'банан', 'бергамот',
                  'дуриан', 'грейпфрут', 'киви', 'лайм', 'лимон', 'локва', 'манго',
                  'дыня', 'нектарин', 'апельсин', 'маракуйя', 'папайя', 'персик',
                  'груша', 'хурма', 'ананас', 'слива', 'гранат', 'помело', 'мандарин',
                  'айва',
                 ]
    return fruit_list


def get_request():
    request = input('Введите первую букву фрукта: ')
    return request
      

def get_result(fruit, request):
    request_fruit = []
    for index in range(len(fruit)):
        if fruit[index].startswith(request):
            request_fruit.append(fruit[index])               
    return request_fruit        
        

if __name__ == '__main__':
    main()