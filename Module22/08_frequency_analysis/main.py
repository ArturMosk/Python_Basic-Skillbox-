import os


def create_list_from_first_tour(file_path):
    file_text = []
    file = open(file_path, 'r')
    for string in file:
        string = string.rstrip('\n')
        file_text.append(string)
    file.close()

    return file_text


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


def create_text_for_result_file(first_text):
    statistics = dict()
    for element in first_text:
        for symbol in element.lower():
            if (symbol in alphabet) and (symbol in statistics):
                statistics[symbol] += 1
            elif (symbol in alphabet) and (symbol not in statistics):
                statistics[symbol] = 1

    total_letters_amt = sum(statistics.values())
    for letter, amount in statistics.items():
        statistics[letter] = round(amount / total_letters_amt, 3)

    frequency_unique = list(reversed(sorted(set(statistics.values()))))

    text_to_file = []
    for frequency in frequency_unique:
        statistics_temp = {alphabet.index(letter): (letter, weight)
                           for letter, weight in statistics.items()
                           if weight == frequency}
        text_to_file.extend([statistics_temp[place] for place in sorted(statistics_temp.keys())])

    return text_to_file


alphabet = 'abcdefghijklmnopqrstuvwxyz'

first_name = 'text.txt'
first_path = os.path.abspath(os.path.join('.', first_name))
second_name = 'analysis.txt'
second_path = os.path.abspath(os.path.join('.', second_name))

first_text_from_file = create_list_from_first_tour(first_path)
text_to_result_file = create_text_for_result_file(first_text_from_file)

create_result_file(text_to_result_file, second_path)

print_file(first_path, first_name)
print_file(second_path, second_name)
