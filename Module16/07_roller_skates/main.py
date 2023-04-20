skates_size = []
feet_size = []

skates_amount = int(input('Кол-во коньков: '))
for index in range(skates_amount):
    print(f'Размер {index + 1}-й пары:', end=' ')
    skate_size = int(input())
    skates_size.append(skate_size)

print()
people_amount = int(input('Кол-во людей: '))
for index in range(people_amount):
    print(f'Размер ноги {index + 1}-го человека:', end=' ')
    foot_size = int(input())
    feet_size.append(foot_size)

feet_size.sort(reverse=True)

count = 0
for foot in feet_size:
    for skate in skates_size:
        if skate >= foot:
            count += 1
            skates_size.remove(skate)
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count)
