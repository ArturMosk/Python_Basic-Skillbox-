def search_exclude_person_index(people, start_index, number_shift):
    index = start_index + number_shift - 1
    if index > len(people) - 1:
        index = index - (index // len(people)) * len(people)

    return index


people_amount = int(input('Кол-во человек: '))
user_number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {user_number}-й человек')

people_list = list(range(1, people_amount + 1))
person_start_index = 0

while len(people_list) > 1:
    print('\nТекущий круг людей:', people_list)
    print('Начало счёта с номера', people_list[person_start_index])
    index_exclude = search_exclude_person_index(people_list, person_start_index, user_number)
    print('Выбывает человек под номером', people_list[index_exclude])
    people_list.remove(people_list[index_exclude])
    if index_exclude <= len(people_list) - 1:
        person_start_index = index_exclude
    else:
        person_start_index = 0

print('\nОстался человек под номером', people_list[0])
