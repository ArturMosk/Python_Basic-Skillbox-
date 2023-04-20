import random

number_amt = int(input('Количество чисел в списке: '))

numbers = [random.randint(0, 2) for _ in range(number_amt)]
print('Список до сжатия:', numbers)

for element in numbers:
    if element == 0:
        numbers.remove(0)
        numbers.append(0)

numbers_compressed = [element for element in numbers if element > 0]

print('Список после сжатия:', numbers_compressed)
