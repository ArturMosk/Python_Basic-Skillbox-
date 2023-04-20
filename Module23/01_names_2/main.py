import os


def create_text_from_file(file_path):
    text_from_file = []
    file = open(file_path, 'r', encoding='utf8')
    for line in file:
        text_from_file.append(line.strip('\n'))
    file.close()

    return text_from_file


def count_and_output_symbols_total(data):
    symbols_amount = 0
    errors = []
    for index, element in enumerate(data):
        try:
            length = len(element)
            if length < 3:
                raise TypeError
            symbols_amount += length

        except TypeError:
            message = f'Ошибка: менее трёх символов в строке {index + 1}'
            print(message)
            errors.append(message + '\n')
    write_errors_log(errors)

    return symbols_amount


def write_errors_log(string):
    with open('errors.log', 'w') as file:
        for line in string:
            file.write(line)


first_name = 'people.txt'
first_path = os.path.abspath(os.path.join('.', first_name))

file_text = create_text_from_file(first_path)
symbols_total = count_and_output_symbols_total(file_text)
print(f'Общее количество символов: {symbols_total}.')
