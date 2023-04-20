guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек:', guests)

    request = input('Гость пришёл или ушёл? ')
    if request == 'Пора спать':
        break

    guest_name = input('Имя гостя: ')

    if request == 'пришёл':
        if len(guests) < 6:
            print(f'Привет, {guest_name}!')
            guests.append(guest_name)
        else:
            print(f'Прости, {guest_name}, но мест нет.')
    elif request == 'ушёл':
        if guest_name in guests:
            guests.remove(guest_name)
            print(f'Пока, {guest_name}!')
        else:
            print('Такого гостя нет!')

print('\nВечеринка закончилась, все легли спать.')