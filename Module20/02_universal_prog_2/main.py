def is_prime(number):
    for digit in [2, 3, 5, 7]:
        if (number <= 1) or (number not in [2, 3, 5, 7]) and (number % digit == 0):
            return False
    return True


def crypto(data):
    return [(value, data[value]) if isinstance(data, dict) else value
            for index, value in enumerate(data) if is_prime(index)]


print(crypto('О Дивный Новый мир!'))
