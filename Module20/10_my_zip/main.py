def my_zip(data_one, data_two):
    length = min(len(data_one), len(data_two))
    result = ((list(data_one)[index], list(data_two)[index]) for index in range(length))

    return result


user_data_one = 'abcd'
user_data_two = 10, 20, 30, 40
print('Строка:', user_data_one)
print('Кортеж чисел:', user_data_two)

print('\nРезультат:')
print(my_zip(user_data_one, user_data_two))
for element in my_zip(user_data_one, user_data_two):
    print(element)
