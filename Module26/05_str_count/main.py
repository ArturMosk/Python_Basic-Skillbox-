import os
from collections.abc import Iterable


def count_amount_code_lines(path_dir: str) -> Iterable[str]:
    """
    Функция, которая берёт все питоновские файлы в директории и вычисляет количество строк в каждом файле,
    игнорируя пустые строки и строки комментариев.

    :param path_dir: путь к директории, в которой происходит поиск питоновских файлов
    :rtype Iterable[int]
    """
    elements = os.listdir(path_dir)
    for element in elements:
        if element.endswith('.py'):
            count = 0
            with open(element, 'r') as file:
                for line in file:
                    line = line.lstrip()
                    line = line.rstrip('\n')
                    if (len(line) > 0) and not line.startswith('#'):
                        count += 1
            yield f'Кол-во строк кода в файле {element} = {count}'


dir_path = '.'
result = count_amount_code_lines(dir_path)
for i_result in result:
    print(i_result)
