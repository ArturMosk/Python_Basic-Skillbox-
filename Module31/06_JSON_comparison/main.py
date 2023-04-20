import json
from typing import Dict


def find_key(struct: Dict, key: str) -> str:
    """
    Функция, реализующая поиск заданного ключа в словаре

    :param struct: словарь для поиска ключа
    :param key: ключ
    :return: значение заданного ключа
    """
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            return find_key(sub_struct, key)


def get_and_output_values_differences(data_old: Dict, data_new: Dict) -> Dict:
    """
    Функция, выполняющая сравнение параметров двух словарей (параметры задаются отдельным списком)
     и вывод их значений в отдельный словарь в случае отличий.

    :param data_old: первый словарь
    :param data_new: второй словарь
    :return: словарь с различающимися параметрами
    """
    values_differences = dict()
    for element in differences:
        element_value_data_old = find_key(data_old, element)
        element_value_data_new = find_key(data_new, element)
        if element_value_data_new != element_value_data_old:
            values_differences[element] = element_value_data_new

    return values_differences


with open('json_old.json', 'r') as file:
    json_old_data = json.load(file)

with open('json_new.json', 'r') as file:
    json_new_data = json.load(file)

differences = ["services", "staff", "datetime"]
result = get_and_output_values_differences(json_old_data, json_new_data)
print(result)

with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)
