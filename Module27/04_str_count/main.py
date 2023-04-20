import functools
from typing import Callable, Any


def counter(function: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции.

    :param function: декорируемая функция
    :rtype: Callable
    """
    starts = [0]

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        starts[0] += 1
        print(f'Декорируемая функция вызвана {starts[0]}-й раз.')
        return function(*args, **kwargs)

    return wrapper


@counter
def test() -> None:
    """
    Декорируемая функция
    """
    print('< Тут что-то происходит >\n')


test()
test()
test()
test()
