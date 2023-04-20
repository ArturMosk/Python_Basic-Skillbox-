from typing import Callable, Any
import functools
import datetime
import traceback


def logging(function: Callable) -> Callable:
    """
    Декоратор, который отвечает за логирование функций.

    :param function: декорируемая функция
    :rtype: Callable
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        print(function.__name__)
        print(function.__doc__)
        try:
            result = function(*args, **kwargs)
        except Exception:
            current_datetime = datetime.datetime.now()
            format_current_datetime = current_datetime.strftime('%d-%m-%Y %H:%M:%S')
            with open('function_errors.log', 'a') as file:
                file.write(format_current_datetime)
                file.write(f"\nFunction's name: {function.__name__}")
                file.write('\n{}\n'.format(traceback.format_exc()))
            return

        return result

    return wrapper


@logging
def test_1(number) -> None:
    """
    Декорируемая функция 1
    """
    number += 1
    return number


@logging
def test_2(number) -> None:
    """
    Декорируемая функция 2
    """
    print(cdd)
    return number


test_1('d')
test_2(50)
