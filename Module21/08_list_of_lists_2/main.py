nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def reconstruct_list_of_lists(data, elements=[]):
    for element in data:
        if isinstance(element, int):
            elements.append(element)
        else:
            reconstruct_list_of_lists(element)

    return elements


only_numbers = reconstruct_list_of_lists(nice_list)
print('Ответ:', only_numbers)
