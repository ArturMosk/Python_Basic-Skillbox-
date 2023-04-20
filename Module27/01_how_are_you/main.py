from typing import Callable, Any
import functools


def how_are_you(function: Callable) -> Callable:
    """
    Декоратор, который при вызове декорируемой функции спрашивает у пользователя «Как дела?»,
    вне зависимости от ответа отвечает что-то вроде «А у меня не очень!»
    и только потом запускает саму функцию.

    :param function: декорируемая функция
    :rtype: Callable
    """

    @functools.wraps(function)
    def wrapped_function(*args, **kwargs) -> Any:
        request = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return function(*args, **kwargs)

    return wrapped_function


@how_are_you
def test() -> None:
    """
    Декорируемая функция
    """
    print('<Тут что-то происходит...>')


test()
