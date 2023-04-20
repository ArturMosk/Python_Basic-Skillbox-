import os


def gen_files_path(search_to_dir: str, search_in_dir='/') -> None:
    """
    Функция, которая реализует поиск указанного каталога и генерирует пути всех встреченных файлов.

    :param search_to_dir: название искомого каталога
    :rtype: str

    :param search_in_dir: название каталога, в котором ведётся поиск
    :rtype: str
    """
    for dir_path, dir_names, file_names in os.walk(search_in_dir):
        if dir_path.endswith(os.path.join(os.path.sep, search_to_dir)):
            print(f'\nИскомая папка {search_to_dir} найдена! Путь к папке:')
            print(dir_path)
            break
        for name in file_names:
            print(os.path.join(dir_path, name))
    else:
        print(f'\nПапка {search_to_dir} не найдена!')


gen_files_path(search_to_dir='PycharmProjects')
