import random

numbers = [random.randint(0, 10) for _ in range(10)]
numbers_new = [(numbers[index], numbers[index + 1]) for index in range(0, 10, 2)]
print('Оригинальный список:', numbers)
print('Новый список:', numbers_new)
