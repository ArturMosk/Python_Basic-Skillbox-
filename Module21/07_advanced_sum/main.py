def sum_for_list(data, elements):
    for element in data:
        if isinstance(element, int):
            elements.append(element)
        else:
            sum_for_list(element, elements)

    return sum(elements)


def my_sum(*args):
    elements_int = []
    for i_arg in args:
        if isinstance(i_arg, list):
            elements_int.append(sum_for_list(i_arg, elements=[]))
        else:
            elements_int.append(i_arg)

    return sum(elements_int)


sum_result = my_sum(1, 2, 3, [4], 5)
print('Сумма чисел из набора параметров:', sum_result)

sum_result = my_sum([[1, 2, [3]], [1], 3])
print('Сумма чисел из списка списков:', sum_result)
