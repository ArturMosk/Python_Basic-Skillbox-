first_list = []
second_list = []

for index in range(3):
    print(f'Введите {index + 1}-е число для первого списка:', end=' ')
    user_number = int(input())
    first_list.append(user_number)

print()
for index in range(7):
    print(f'Введите {index + 1}-е число для второго списка:', end=' ')
    user_number = int(input())
    second_list.append(user_number)

print('\nПервый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)

for element in first_list:
    while first_list.count(element) > 1:
        first_list.remove(element)

print('\nНовый первый список с уникальными элементами: ', first_list)