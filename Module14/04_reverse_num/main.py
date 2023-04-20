def reverse_integer_part(number):
    number_str = str(int(number))
    number_str_reversed = ''
    for element in reversed(number_str):
        number_str_reversed += element

    number_reversed = int(number_str_reversed)

    return number_reversed


def reverse_decimal_part(number):
    number_str = str(number)

    for index in range(len(number_str)):
        if number_str[index] == '.':
            number_decimal_part_str = number_str[index + 1:]
            break

    number_decimal_part_str_reversed = ''
    for element in reversed(number_decimal_part_str):
        number_decimal_part_str_reversed += element

    count = len(number_decimal_part_str_reversed)
    number_decimal_part_reversed = int(number_decimal_part_str_reversed)
    number_decimal_part_reversed /= 10 ** count

    return number_decimal_part_reversed


user_number_one = float(input('Введите первое число: '))
user_number_two = float(input('Введите второе число: '))

user_number_integer_part_reversed = reverse_integer_part(user_number_one)
user_number_decimal_part_reversed = reverse_decimal_part(user_number_one)
user_number_one_reversed = user_number_integer_part_reversed + user_number_decimal_part_reversed
print('\nПервое число наоборот:', user_number_one_reversed)

user_number_integer_part_reversed = reverse_integer_part(user_number_two)
user_number_decimal_part_reversed = reverse_decimal_part(user_number_two)
user_number_two_reversed = user_number_integer_part_reversed + user_number_decimal_part_reversed
print('Второе число наоборот:', user_number_two_reversed)

sum_user_numbers_reversed = user_number_one_reversed + user_number_two_reversed
print('Сумма:', sum_user_numbers_reversed)
