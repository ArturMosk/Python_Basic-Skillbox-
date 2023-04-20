def print_numbers_from_1_to_num(num):
    if num > 0:
        print_numbers_from_1_to_num(num - 1)
        print(num)


user_number = int(input('Введите num: '))
print_numbers_from_1_to_num(user_number)
