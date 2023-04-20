from collections.abc import Iterable


def find_necessary_result(target_number: int) -> Iterable[int]:
    """
    Функция-генератор, реализующая поиск заданного числа, которое может получиться
     в результате попарного перемножения двух чисел из заданных списков.

    :param target_number: искомое значение
    :rtype int

    :return: None, выход из циклов
    """
    for number_x in numbers_1:
        for number_y in numbers_2:
            result = number_x * number_y
            print(number_x, number_y, result)
            if result == target_number:
                yield 'Found!!!'
                return


numbers_1 = [2, 5, 7, 10]
numbers_2 = [3, 8, 4, 9]
to_find = 56

search_result = find_necessary_result(to_find)
for element in search_result:
    print(element)
