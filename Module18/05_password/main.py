while True:
    password = input('Придумайте пароль: ')

    digit_count = 0
    flag = False

    for element in password:
        if element.isupper():
            flag = True
        if element.isdigit():
            digit_count += 1

    if (len(password) < 8) or (not flag) or (digit_count < 3):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
