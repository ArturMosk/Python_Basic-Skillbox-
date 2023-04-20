def read_current_chat():
    try:
        with open('chat.txt', 'r') as file:
            for line in file:
                print(line, end='')
        print()
    except FileNotFoundError:
        print('В чате нет сообщений.')


def send_message_to_chat(name):
    message = input('\nВведите сообщение: ')
    with open('chat.txt', 'a') as file:
        file.write(f'\n\n{name}:\n')
        file.write(f'{message}')


user_name = input('Введите имя: ')
print(f'{user_name}, добро пожаловать в общий чат!')
while True:
    print('\nВыберите действие:')
    print('     1 - Посмотреть текущий текст чата')
    print('     2 - Отправить сообщение')
    user_choice = input('>> ')
    if user_choice == '1':
        read_current_chat()
    elif user_choice == '2':
        send_message_to_chat(user_name)
    else:
        print('Некорректный ввод! Нужно ввести 1 или 2.')
