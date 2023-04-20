def add_records_and_form_table_results(records, number):
    print('Записи (результат и имя):')
    for i_record in range(1, number + 1):
        print(f'{i_record}-я запись: ', end='')
        record = input().split()
        records[i_record] = (int(record[0]), record[1])


def search_and_print_winners(records):
    max_result = 0
    max_name = ''
    for number in sorted(records.keys()):
        if records[number][0] > max_result:
            max_result = records[number][0]
            max_name = records[number][1]

    return max_name, max_result


def remove_winner_name_from_table_results(records, player):
    records_new = dict()
    for number, record in records.items():
        if record[1] != player:
            records_new[number] = record

    return records_new


records_amt = int(input('Сколько записей вносится в протокол? '))
table_results = dict()
add_records_and_form_table_results(table_results, records_amt)

print()
for index in range(1, 4):
    name, result = search_and_print_winners(table_results)
    print(f'{index}-е место. {name} ({result})')
    table_results = remove_winner_name_from_table_results(table_results, name)
