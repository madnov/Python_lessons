from random import randint
from random import choice

numbers = [randint(1, 10) for _ in range(15)]
print(numbers)
result = sorted([choice(numbers) for _ in range(randint(1, len(numbers)))])
# result = list(
#     filter(lambda x: [choice(numbers) for i in range(randint(1, len(numbers)))], numbers))
print(result)
