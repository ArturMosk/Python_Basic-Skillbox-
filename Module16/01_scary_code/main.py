list_a = [1, 5, 3]
list_b = [1, 5, 1, 5]
list_c = [1, 3, 1, 5, 3, 3]

print('\nРезультат работы программы:')

list_a.extend(list_b)
digit_five_amt = list_a.count(5)
print('Кол-во цифр 5 при первом объединении:', digit_five_amt)

for element in list_a:
    if element == 5:
        list_a.remove(element)

list_a.extend(list_c)
digit_three_amt = list_a.count(3)
print('Кол-во цифр 3 при втором объединении:', digit_three_amt)

print('Итоговый список:', list_a)