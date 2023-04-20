import os


def create_list(file_path):
    file_text = []
    file = open(file_path, 'r')
    for string in file:
        string = string.rstrip('\n')
        file_text.append(string)
    file.close()

    return file_text


def cesar_crypt(line, shift):
    line_encrypted = ''
    for symbol in line:
        i_alphabet = list(alphabet).index(symbol.lower())
        i_new = i_alphabet + shift
        if i_new > len(alphabet) - 1:
            i_new = i_new - len(alphabet) * (i_new // len(alphabet))

        if symbol.isupper():
            line_encrypted += alphabet[i_new].upper()
        else:
            line_encrypted += alphabet[i_new]

    return line_encrypted


def encrypt_text(text):
    text_encrypted = []
    step = 1
    for element in text:
        element_encrypted = cesar_crypt(element, step)
        text_encrypted.append(element_encrypted)
        step += 1

    return text_encrypted


def create_encrypted_file(text, file_path):
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


alphabet = 'abcdefghijklmnopqrstuvwxyz'

file_name = 'text.txt'
path_file_name = os.path.abspath(os.path.join('.', file_name))
file_encrypted_name = 'cipher_text.txt'
path_file_encrypted_name = os.path.abspath(os.path.join('.', file_encrypted_name))

text_from_file = create_list(path_file_name)
text_encrypted_from_file = encrypt_text(text_from_file)
create_encrypted_file(text_encrypted_from_file, path_file_encrypted_name)

print_file(path_file_name, file_name)
print_file(path_file_encrypted_name, file_encrypted_name)
