import os
import zipfile


def create_text_from_first_file(file_path):
    file_text = []
    file = open(file_path, 'r', encoding='utf8')
    for string in file:
        string = string.rstrip('\n')
        file_text.append(string)
    file.close()

    return file_text


def create_text_for_result_file(first_text):
    statistics = dict()
    for element in first_text:
        for symbol in element:
            if (symbol in statistics) and symbol.isalpha():
                statistics[symbol] += 1
            elif (symbol not in statistics) and symbol.isalpha():
                statistics[symbol] = 1

    statistics_replaced = {amount: letter for letter, amount in statistics.items()}
    text_to_file = [(statistics_replaced[amount], amount)
                    for amount in reversed(sorted(statistics_replaced.keys()))]

    return text_to_file


def create_result_file(text, file_path):
    file = open(file_path, 'w')
    for letter, frequency in text:
        file.write(letter + ' ' + str(frequency) + '\n')
    file.close()


def print_file(file_path, name):
    print(f'\nСодержимое файла {name}:')
    file = open(file_path, 'r')
    for line in file:
        print(line, end='')
    print()
    file.close()


archive = 'voyna-i-mir.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall('.')

first_name = 'voyna-i-mir.txt'
first_path = os.path.abspath(os.path.join('.', first_name))
second_name = 'statistic.txt'
second_path = os.path.abspath(os.path.join('.', second_name))

first_text_from_file = create_text_from_first_file(first_path)
text_to_result_file = create_text_for_result_file(first_text_from_file)

create_result_file(text_to_result_file, second_path)

print_file(second_path, second_name)
