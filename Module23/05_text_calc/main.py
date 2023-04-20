def choose_action_and_output_result(string):
    actions_maths = ['+', '-', '*', '/', '//', '%']
    elements = string.split()
    try:
        if elements[1] in actions_maths and (len(elements) == 3):
            if elements[1] == '+':
                result = int(elements[0]) + int(elements[2])
            elif elements[1] == '-':
                result = int(elements[0]) - int(elements[2])
            elif elements[1] == '*':
                result = int(elements[0]) * int(elements[2])
            elif elements[1] == '/':
                result = int(elements[0]) / int(elements[2])
            elif elements[1] == '//':
                result = int(elements[0]) // int(elements[2])
            elif elements[1] == '%':
                result = int(elements[0]) % int(elements[2])

            return result

        else:
            return request_action_in_case_error(string)

    except IndexError:
        return request_action_in_case_error(string)
    except ValueError:
        return request_action_in_case_error(string)


def request_action_in_case_error(string_error):
    while True:
        print(f'Обнаружена ошибка в строке: {string_error}     Хотите исправить? ', end='')
        answer = input().lower()
        if answer == "да":
            new_string = input('Введите исправленную строку: ')
            return choose_action_and_output_result(new_string)
        elif answer == 'нет':
            return None


with open('calc.txt', 'r') as file:
    actions_sum = 0
    for line in file:
        line = line.strip('\n')
        if len(line) != 0:
            action_result = choose_action_and_output_result(line)
            if action_result:
                actions_sum += action_result

print('\nСумма результатов:', actions_sum)
