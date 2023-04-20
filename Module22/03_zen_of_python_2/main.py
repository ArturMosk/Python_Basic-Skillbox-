import os


def read_file_and_create_list(path):
    file_lines = []
    file = open(path, 'r')
    for line in file:
        file_lines.append(line)
    file.close()

    return file_lines


def find_letters_amount_and_the_rarest_letter(strings):
    letters = dict()
    for string in strings:
        string = string.rstrip('\n')
        for symbol in string.lower():
            if symbol.isalpha() and symbol in letters:
                letters[symbol] += 1
            elif symbol.isalpha() and symbol not in letters:
                letters[symbol] = 1

    letters_total = sum(letters.values())

    letters_rarest = ''
    amount_min = min(letters.values())
    for letter, amount in letters.items():
        if amount == amount_min:
            letters_rarest += letter + ' '

    return letters_total, letters_rarest


def count_and_output_words_amount(strings):
    words = []
    for string in strings:
        words.extend(string.split())

    count = 0
    for word in words:
        for symbol in word:
            if symbol.isalpha():
                count += 1
                break

    return count


file_path = os.path.join('..', '02_zen_of_python', 'zen.txt')
lines = read_file_and_create_list(file_path)

letters_amt, letter_min = find_letters_amount_and_the_rarest_letter(lines)  # кол-во букв и самая редкая буква
words_amt = count_and_output_words_amount(lines)  # кол-во слов
strings_amt = len(lines)  # кол-во строк

print()
print('Количество букв в файле:', letters_amt)
print('Количество слов в файле:', words_amt)
print('Количество строк в файле:', strings_amt)
print('Наиболее редкая буква:', letter_min)
