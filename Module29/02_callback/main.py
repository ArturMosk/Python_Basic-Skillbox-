import functools
from collections.abc import Callable


def callback(symbols: str):
    """
    Декоратор. Функция обратного вызова.
    """

    def check_callback(func: Callable) -> Callable:
        """
        Декорируемый декоратор, вызывающий функцию при срабатывании определённого события.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            app = {symbols: 'адрес сайта'}
            route = app.get('//')
            if route:
                response = func(*args, **kwargs)
                print('Ответ:', response)
            else:
                print('Такого пути нет')
            return

        return wrapper

    return check_callback


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


example()
