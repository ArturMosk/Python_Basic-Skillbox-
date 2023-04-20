import random


def numbers_plus_random(number_x, number_y):
    number_x -= random.randint(0, 10)
    number_y -= random.randint(0, 5)
    try:
        result = number_x / number_y
    except ZeroDivisionError:
        print("Деление на ноль в первой функции")
    return result


def numbers_minus_random(number_x, number_y):
    number_x -= random.randint(0, 10)
    number_y -= random.randint(0, 5)
    try:
        result = number_y / number_x
    except ZeroDivisionError:
        print("Деление на ноль во второй функции")
    return result


my_results = []
try:
    with open('coordinates.txt', 'r') as file_data:
        for index, line in enumerate(file_data):
            nums_list = line.split()
            res1 = numbers_plus_random(int(nums_list[0]), int(nums_list[1]))
            res2 = numbers_minus_random(int(nums_list[0]), int(nums_list[1]))

            number = random.randint(0, 100)
            line_results = [str(element) for element in sorted([res1, res2, number])]
            my_results.append('  '.join(line_results) + '\n')

    with open('result.txt', 'w') as file_result:
        file_result.write(''.join(my_results))

except FileNotFoundError:
    print('Отсутствует файл с координатами.')

except ValueError:
    print('Невозможно преобразовать входные данные в целое число!')

except UnboundLocalError:
    print(f'Недопустимый результат, возвращаемый функцией из строки {index + 1}!')

except TypeError:
    print('Попытка записи в файл результатов не строковых данных.')
