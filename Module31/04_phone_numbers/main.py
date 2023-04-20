import re

phone_numbers = ['9999999999', '999999-999', '99999x9999']

for index, i_number in enumerate(phone_numbers):
    phone_number_pattern = r'[89]\d{9}'
    if re.match(phone_number_pattern, i_number) and len(i_number) == 10:
        print(f'{index + 1}-й номер: всё в порядке')
    else:
        print(f'{index + 1}-й номер: не подходит')
