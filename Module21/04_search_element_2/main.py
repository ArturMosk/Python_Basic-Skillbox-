site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_and_output_value(data, key, depth=None):
    if key in data:
        return data[key]

    result = None
    if not depth:
        for sub_data in data.values():
            if isinstance(sub_data, dict):
                result = search_and_output_value(sub_data, key)
                if result:
                    break
    elif depth > 1:
        for sub_data in data.values():
            if isinstance(sub_data, dict):
                depth -= 1
                result = search_and_output_value(sub_data, key, depth)
                if result:
                    break

    return result


user_key = input('Введите искомый ключ: ')

while True:
    depth_request = input('Хотите ввести максимальную глубину? Y/N: ').lower()
    if depth_request == 'y':
        depth_amt = int(input('Введите максимальную глубину: '))
        value_searched = search_and_output_value(site, user_key, depth=depth_amt)
        break
    elif depth_request == 'n':
        value_searched = search_and_output_value(site, user_key)
        break

if value_searched:
    print('Значение ключа:', value_searched)
else:
    print('Такого ключа в структуре сайта нет.')
