numbers_amount = int(input('Кол-во чисел: '))

numbers = []
for _ in range(numbers_amount):
    number = int(input('Число: '))
    numbers.append(number)

print('\nПоследовательность:', numbers)

add_numbers = []
flag = True
while flag and len(numbers) > 1:
    for index in range(len(numbers) // 2):
        if numbers[index] == numbers[-(index + 1)]:
            flag = False
        else:
            add_numbers.append(numbers[0])
            numbers.pop(0)
            flag = True
            break

add_numbers.reverse()

print('Нужно приписать чисел:', len(add_numbers))
print('Сами числа:', add_numbers)
