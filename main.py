
with open('appel.txt', 'r', encoding='utf-8') as file:
    question = file.read().replace('\n', ':').split(':')
    

    
print(question)

