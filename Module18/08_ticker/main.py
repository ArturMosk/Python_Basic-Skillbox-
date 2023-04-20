text_one = input('Первая строка: ')
text_two = input('Вторая строка: ')

flag = False
for index in range(1, len(text_two) + 1):
    text_two = text_two[-1] + text_two[:-1]
    if text_two == text_one:
        print(f'\nПервая строка получается из второй со сдвигом {index}.')
        flag = True

if not flag:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
