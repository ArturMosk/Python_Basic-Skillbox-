def print_file(file_name):
    print('\nСодержимое файла', file_name)
    file = open(file_name, 'r')
    for i_line in file:
        print(i_line, end='')
    file.close()
    print()


def count_and_output_numbers_sum(file_name):
    file = open(file_name, 'r')
    numbers_sum = 0
    for i_line in file:
        elements = i_line.split()
        for element in elements:
            if element.isdigit():
                numbers_sum += int(element)
    file.close()

    return numbers_sum


def create_file_answer(file_numbers_sum):
    file = open('answer.txt', 'w')
    file.write(str(file_numbers_sum))
    file.close()


print_file('numbers.txt')
file_sum = count_and_output_numbers_sum('numbers.txt')
create_file_answer(file_sum)
print_file('answer.txt')
