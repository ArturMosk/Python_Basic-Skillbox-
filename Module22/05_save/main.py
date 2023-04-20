import os


def create_path_to_file(path):
    dirs_names = path.split()
    path_to_file_str = ''
    for name in dirs_names:
        path_to_file_str += name + os.path.sep

    path_to_file = os.path.abspath(os.path.join(os.path.sep, path_to_file_str))

    return path_to_file


def record_user_text_to_file(file_text, path, file_name):
    file_name += '.txt'
    file_path = os.path.join(path, file_name)
    if os.path.exists(file_path):
        while True:
            request = input('\nВы действительно хотите перезаписать файл? ')
            if request.lower() == 'да':
                file_message = 'Файл успешно перезаписан!'
                write_text_and_print_file(file_text, file_path, file_name, file_message)
                break
            elif request.lower() == 'нет':
                print('Программа завершена!')
                break
            print("Некорректный ответ! Введите 'да' или 'нет'.")
    else:
        file_message = 'Файл успешно сохранён!'
        write_text_and_print_file(file_text, file_path, file_name, file_message)


def write_text_and_print_file(text, path, name, message):
    file = open(path, 'w')
    file.write(text)
    file.close()
    print(message)

    print(f'\nСодержимое файла {name}:')
    file = open(path, 'r')
    for line in file:
        print(line, end='')
    file.close()


user_text = input('Введите строку: ')

print('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел): ')
user_path = input('>> ')

user_file_name = input('\nВведите имя файла: ')

dirs_path = create_path_to_file(user_path)
if os.path.exists(dirs_path):
    record_user_text_to_file(user_text, dirs_path, user_file_name)
else:
    print('\nСохранить документ по указанному пути нельзя! Такого пути не существует!')
