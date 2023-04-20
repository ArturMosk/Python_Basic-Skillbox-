import time
from typing import Callable, Any
import functools


def sleep(function: Callable) -> Callable:
    """
    Декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

    :param function: декорируемая функция
    :rtype: Callable
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        time.sleep(3)
        return function(*args, **kwargs)

    return wrapper


@sleep
def test() -> None:
    """
    Декорируемая функция
    """
    print('< Тут что-то происходит\n с задержкой в 3 секунды перед началом выполнения >')


test()
