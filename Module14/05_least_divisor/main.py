def count_and_output_min_divider(number):
    flag = True
    for digit in (2, 3, 5, 7):
        if number % digit == 0:
            print('Наименьший делитель, отличный от единицы:', digit)
            flag = False
            break

    if flag:
        print('Наименьший делитель, отличный от единицы:', number)


user_number = int(input('Введите число: '))
if user_number <= 1:
    print('Ошибка ввода! Число должно быть натуральным и больше 1.')
else:
    count_and_output_min_divider(user_number)
