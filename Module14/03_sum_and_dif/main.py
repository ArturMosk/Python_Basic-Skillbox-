def count_sum_of_digits(number):
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number //= 10

    return sum_of_digits


def count_number_of_digits(number):
    count_of_digits = 0
    while number > 0:
        count_of_digits += 1
        number //= 10

    return count_of_digits


user_number = int(input('\nВведите число: '))
if user_number <= 0:
    print('\nОшибка ввода! Число должно быть целым и положительным.')
else:
    user_number_sum = count_sum_of_digits(user_number)
    user_number_count = count_number_of_digits(user_number)
    difference_sum_and_count = user_number_sum - user_number_count

    print('\nСумма чисел:', user_number_sum)
    print('Количество цифр в числе:', user_number_count)
    print('Разность суммы и количества цифр:', difference_sum_and_count)
