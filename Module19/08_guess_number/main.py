import random

number_max = int(input('Введите максимальное число: '))

number_rnd = random.randint(1, number_max)

numbers_possible = set()
while True:
    numbers = set()
    request = input('\nНужное число есть среди вот этих чисел: ')
    if request == 'Помогите!':
        print('Артём мог загадать следующие числа: ', end='')
        for elem in sorted(numbers_possible):
            if elem <= number_max:
                print(elem, end=' ')
        break

    user_numbers = request.split()
    for number in user_numbers:
        numbers.add(int(number))

    if number_rnd in numbers:
        print('Ответ Артёма: Да')
        if len(numbers_possible) == 0:
            numbers_possible.update(numbers)
        else:
            numbers_possible.intersection_update(numbers)
    else:
        print('Ответ Артёма: Нет')
        numbers_possible.difference_update(numbers)
