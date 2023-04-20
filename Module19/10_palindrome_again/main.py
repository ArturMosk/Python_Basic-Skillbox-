# Согласно моим соображениям,
# если в строке больше одного уникального символа с нечетным количеством элементов,
# то палиндром сделать нельзя.

def if_palindrom_possible(string):
    letters = list(string)
    letters_unique = set(letters)
    count = 0
    is_flag = True
    for element in letters_unique:
        if letters.count(element) % 2 != 0:
            count += 1

    if count > 1:
        is_flag = False

    return is_flag


user_string = input('Введите строку: ').lower()
flag = if_palindrom_possible(user_string)
if flag:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
