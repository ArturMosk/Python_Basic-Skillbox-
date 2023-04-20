def slicer(data, number):
    if data.count(number) == 0:
        data = list(data)
        data = []
        return tuple(data)
    elif data.count(number) == 1:
        i_number = data.index(number)
        return data[i_number:]
    else:
        count = 0
        for index, value in enumerate(data):
            if value == number:
                if count == 0:
                    index_start = index
                    count = 1
                elif count == 1:
                    return data[index_start: index + 1]


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
