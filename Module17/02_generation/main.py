length = int(input('Введите длину списка: '))

numbers = [1 if index % 2 == 0 else index % 5 for index in range(length)]

print('Результат:', numbers)
