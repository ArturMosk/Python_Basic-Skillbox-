from collections.abc import Iterable


class SquareNumber:
    """
    Класс-итератор, реализующий последовательность из квадратов чисел от 1 до N

    Args:
        number_n (int): значение числа N
    """

    def __init__(self, number_n: int) -> None:
        self.number_n = number_n
        self.counter = 0

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> int:
        self.counter += 1
        if self.counter > self.number_n:
            raise StopIteration

        return self.counter ** 2


def generate_square_numbers(number_n: int) -> Iterable[int]:
    """
    Функция-генератор, реализующая последовательность из квадратов чисел от 1 до N

    :param number_n: значение числа N
    :rtype: Iterable[int]
    """
    for number in range(1, number_n + 1):
        yield number ** 2


user_number = int(input('Введите число: '))
print(f'\nПоследовательность из квадратов чисел от 1 до {user_number}:')

# Реализация класса-итератора
print('\033[31m{}\033[0m'.format(f'---- Реализация класса-итератора ----'))
square_numbers_1 = SquareNumber(user_number)
for i_number in square_numbers_1:
    print(i_number, end=' ')

# Реализация функции-генератора
print('\n')
print('\033[31m{}\033[0m'.format(f'---- Реализация функции-генератора ----'))
square_numbers_2 = generate_square_numbers(user_number)
for i_number in square_numbers_2:
    print(i_number, end=' ')

# Реализация генераторного выражения
print('\n')
print('\033[31m{}\033[0m'.format(f'---- Реализация генераторного выражения ----'))
square_numbers_3 = (number ** 2 for number in range(1, user_number + 1))
for i_number in square_numbers_3:
    print(i_number, end=' ')
print()
