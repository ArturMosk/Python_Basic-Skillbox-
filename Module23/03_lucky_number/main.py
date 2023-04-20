import random

numbers_sum = 0
with open('out_file.txt', 'w') as file:
    while True:
        try:
            user_number = int(input('Введите число: '))
            numbers_sum += user_number
            if numbers_sum < 777:
                if 13 == random.randint(1, 13):
                    raise BaseException
                file.write(str(user_number) + '\n')
            else:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                file.write(str(user_number))
                break

        except ValueError:
            print('Введённое значение нельзя преобразовать в целое число!')

        except BaseException:
            print('Вас постигла неудача!')
            break

print('\nСодержимое файла out_file.txt:')
with open('out_file.txt', 'r') as file:
    for line in file:
        print(line, end='')
