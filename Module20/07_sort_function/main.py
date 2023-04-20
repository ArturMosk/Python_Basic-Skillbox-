def sort_and_output_data(data):
    data = list(data)
    for element in data:
        if not isinstance(element, int):
            data = []
            return tuple(data)

    for index, value in enumerate(data):
        value_min = min(data[index:])
        data.remove(value_min)
        data.insert(index, value_min)

    return tuple(data)


print(sort_and_output_data((6, 3, -1, 8, 4, 10, -5)))
