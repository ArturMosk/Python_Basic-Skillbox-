import time
import functools
from datetime import datetime
from collections.abc import Callable


def timer(cls, func: Callable, date_format: str) -> Callable:
    """ Декоратор. Выводит время запуска и время работы метода класса. """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        format = date_format
        for symbol in format:
            if symbol.isalpha():
                format = format.replace(symbol, '%' + symbol)

        print(f"- Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(format)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"- Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
        return result

    return wrapped


def log_methods(date_format: str):
    """
    Декоратор, логирующий все методы декорируемого класса (кроме магических методов),
    и в который можно передавать формат вывода даты и времени логирования.
    """
    @functools.wraps(timer)
    def decorate(cls):
        for i_method_name in dir(cls):
            if not i_method_name.startswith('__'):
                current_method = getattr(cls, i_method_name)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, i_method_name, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class First:
    """
    Родительский класс, содержащий некие методы.
    """
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class Second(First):
    """
    Наследуемый класс. Класс-родитель First.
    """
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = Second()
my_obj.test_sum_1()
my_obj.test_sum_2()
