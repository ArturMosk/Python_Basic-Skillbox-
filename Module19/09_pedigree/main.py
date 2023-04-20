def create_genealogical_pairs(people_amt):
    gen_pairs = dict()
    for i_pair in range(1, people_amt):
        print(f'{i_pair}-я пара: ', end='')
        pair = input()
        pairs = pair.split()
        gen_pairs[pairs[0]] = pairs[1]

    return gen_pairs


def search_and_form_members_height(gen_pairs, members, member_height):
    members_current = set()
    descendants_current = set()
    for member, height in members.items():
        if height == member_height:
            members_current.add(member)

    for descendant, parent in gen_pairs.items():
        if parent in members_current:
            descendants_current.add(descendant)

    return descendants_current


def print_members_heights_by_alphabet(members):
    print()
    print('«Высота» каждого члена семьи:')
    for member in sorted(members.keys()):
        print(member, members[member])


people_amount = int(input('Введите количество человек: '))

genealogical_pairs = create_genealogical_pairs(people_amount)

members_heights = dict()
for parent in genealogical_pairs.values():
    if parent not in genealogical_pairs.keys():
        members_heights[parent] = 0
        break

for index in range(len(genealogical_pairs.values())):
    descendants = search_and_form_members_height(genealogical_pairs, members_heights, index)
    for descendant in descendants:
        members_heights[descendant] = index + 1

print_members_heights_by_alphabet(members_heights)
