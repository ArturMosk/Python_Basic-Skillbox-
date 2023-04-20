def check_for_correct_data(string):
    elements = string.split()
    try:
        if len(elements) < 3:
            raise IndexError
        elif not elements[0].isalpha():
            raise NameError
        elif ('@' not in elements[1]) and ('.' not in elements[1]):
            raise SyntaxError
        elif (int(elements[2]) < 10) or (int(elements[2]) > 99):
            raise ValueError

    except IndexError:
        return 'НЕ присутствуют все три поля'
    except NameError:
        return 'Поле «Имя» содержит НЕ только буквы'
    except SyntaxError:
        return 'Поле «Имейл» НЕ содержит @ и . (точку)'
    except ValueError:
        return 'Поле «Возраст» НЕ является числом от 10 до 99'


file_good = open('registrations_good.log', 'w')
file_bad = open('registrations_bad.log', 'w')
with open('registrations.txt', 'r', encoding='utf-8') as file_data:
    for line in file_data:
        line = line.strip('\n')
        result = check_for_correct_data(line)
        if result:
            file_bad.write(line + '\t\t\t\t' + result + '\n')
        else:
            file_good.write(line + '\n')

file_good.close()
file_good.close()
