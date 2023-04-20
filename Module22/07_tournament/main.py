import os


def create_list_from_first_tour(file_path):
    file_text = []
    file = open(file_path, 'r')
    for string in file:
        string = string.rstrip('\n').split()
        file_text.append(string)
    file.close()

    return file_text


def create_second_file(text, file_path):
    file = open(file_path, 'w')
    for element in text:
        file.write(element + '\n')
    file.close()


def print_file(file_path, name):
    print(f'\nСодержимое файла {name}:')
    file = open(file_path, 'r')
    for line in file:
        print(line, end='')
    print()
    file.close()


def create_text_for_second_tour(first_text):
    barrier = int(first_text[0][0])

    first_text.remove(first_text[0])
    first_text_modified = dict()
    for element in first_text:
        first_text_modified[int(element[2])] = element[1][0] + '. ' + element[0]

    second_text = []
    place = 1
    for rating in reversed(sorted(first_text_modified.keys())):
        if rating > barrier:
            temp_str = f'{place}) {first_text_modified[rating]} {rating}'
            second_text.append(temp_str)
        else:
            break
        place += 1

    second_text.insert(0, str(len(second_text)))

    return second_text


first_name = 'first_tour.txt'
first_path = os.path.abspath(os.path.join('.', first_name))
second_name = 'second_tour.txt'
second_path = os.path.abspath(os.path.join('.', second_name))

first_text_from_file = create_list_from_first_tour(first_path)
second_text_to_file = create_text_for_second_tour(first_text_from_file)

create_second_file(second_text_to_file, second_path)

print_file(first_path, first_name)
print_file(second_path, second_name)
