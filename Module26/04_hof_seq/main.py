from collections.abc import Iterable


def q_hofstadter_generator(start_numbers: list) -> Iterable[int]:
    """
    Функция-генератор, реализующая генерацию последовательности Q Хофштадтера.

    :param start_numbers: список из двух чисел, передающийся в генератор
    :rtype: list

    :return выход из функции
    """
    if start_numbers == [1, 2]:
        print('\nВ функцию переданы значения [1, 2]! Передайте другие значения.')
        return
    sequence = start_numbers[:]
    while True:
        try:
            q_next = sequence[-sequence[-1]] + sequence[-sequence[-2]]
            sequence.append(q_next)
            yield q_next
        except IndexError:
            return


result = q_hofstadter_generator([1, 1])
for q_element in result:
    print(q_element)
