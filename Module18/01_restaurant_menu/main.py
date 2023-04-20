menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
print('Доступное меню: ', menu)

menu_lst = menu.split(';')
menu_modified = ', '.join(menu_lst)

print('\nНа данный момент в меню есть:', menu_modified)
