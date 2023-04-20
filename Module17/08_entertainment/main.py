import random

sticks_amount = int(input('Количество палок: '))
hits_amount = int(input('Количество бросков: '))

sticks_condition = ['I' for element in range(sticks_amount)]

for index in range(1, hits_amount + 1):
    left_i = random.randint(1, sticks_amount)
    right_i = random.randint(1, sticks_amount)
    if left_i > right_i:
        left_i, right_i = right_i, left_i
    print(f'Бросок {index}. Сбиты палки с номера {left_i} \nпо номер {right_i}.')
    sticks_condition[left_i - 1: right_i] = ['.' for element in range(right_i - left_i + 1)]

sticks_condition_str = ''
for element in sticks_condition:
    sticks_condition_str += element

print('Результат:', sticks_condition_str)
