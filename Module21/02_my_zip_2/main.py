def my_zip(*args):
    length = min([len(i_data) for i_data in args])
    result = [tuple([list(i_data)[index] for i_data in args]) for index in range(length)]

    return result


user_data_one = [1, 2, 3, 4, 5]
user_data_two = {1: "s", 2: "q", 3: 4}
user_data_three = (1, 2, 3, 4, 5)

print('\nРезультат:')
my_zip_result = my_zip(user_data_one, user_data_two, user_data_three)
print(my_zip_result)
