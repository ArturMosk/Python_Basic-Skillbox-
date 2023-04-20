friends_amount = int(input('Кол-во друзей: '))
ious_amount = int(input('Долговых расписок: '))

notes = []
for index in range(ious_amount):
    note = []
    print(f'{index + 1}-я расписка')
    person_to = input('Кому: ')
    note.append(person_to)
    person_from = input('От кого: ')
    note.append(person_from)
    debt = int(input('Сколько: '))
    note.append(debt)
    notes.append(note)
    print()

friends_debt_list = []
for _ in range(friends_amount):
    friends_debt_list.append(0)

for note in notes:
    index_to = int(note[0]) - 1
    friends_debt_list[index_to] -= int(note[2])
    index_from = int(note[1]) - 1
    friends_debt_list[index_from] += int(note[2])

print('Баланс друзей:')
for index in range(len(friends_debt_list)):
    print(f'{index + 1}: {friends_debt_list[index]}')