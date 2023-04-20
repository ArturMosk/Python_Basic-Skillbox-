def check_and_add_contact(phonebook):
    print('Введите имя и фамилию нового контакта (через пробел): ', end='')
    person = input()
    person = tuple(person.split())
    for name, surname in phonebook:
        if (name.lower() == person[0].lower()) and (surname.lower() == person[1].lower()):
            print('Такой человек уже есть в контактах.')
            return

    number = int(input('Введите номер телефона: '))
    phonebook[person] = number


def search_and_print_person(phonebook):
    surname = input('Введите фамилию для поиска: ').lower()
    for person, number in phonebook.items():
        if person[1].lower() == surname:
            print(person[0], person[1], number)


contacts = dict()
while True:
    print('\nВведите номер действия:')
    print('  1. Добавить контакт')
    print('  2. Найти человека')
    action = int(input())
    if action == 1:
        check_and_add_contact(contacts)
        print('Текущий словарь контактов:', contacts)
    elif action == 2:
        search_and_print_person(contacts)
