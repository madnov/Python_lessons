numbers = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
def main(numbers):
    for i in range(len(numbers)//2):
        if numbers.count(numbers[i]) % 2 != 0:
            return numbers[i]
print(main(numbers))