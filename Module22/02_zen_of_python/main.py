def print_reversed_file(file_name):
    file = open(file_name, 'r')
    lines = []
    for i_line in file:
        lines.append(i_line)
    file.close()

    print(lines[-1])
    for line in lines[-2::-1]:
        print(line, end='')


print_reversed_file('zen.txt')
