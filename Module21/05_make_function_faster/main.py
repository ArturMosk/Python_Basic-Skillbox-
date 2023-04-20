def calculating_math_func(number, data):
    if number in data:
        return data[number]

    result = 1
    for index in range(1, number + 1):
        result *= index
    result /= number ** 3
    result = result ** 10
    data[number] = result
    return result


data_results = dict()
for user_number in [3, 4, 5, 6, 3, 4]:
    calc = calculating_math_func(user_number, data_results)
    print(calc)

print(data_results)
