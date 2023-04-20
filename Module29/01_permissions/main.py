import functools
from collections.abc import Callable


def check_permission(user_name: str):
    """
    Декоратор, который проверяет, есть ли у передаваемого пользователя доступ к вызываемой функции.
    """

    def check_decorator(func: Callable) -> Callable:
        """
        Декорируемый декоратор, вызывающий функцию для проверки доступа.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user_name in user_permissions:
                func(*args, **kwargs)
            else:
                print('{error}: У пользователя {user} недостаточно прав, чтобы выполнить функцию {name}'.format(
                    error='PermissionError', user=user_name, name=func.__name__
                ))
            return

        return wrapper

    return check_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    """ Декорируемая функция, реализующая удаление сайта. """
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    """ Декорируемая функция, реализующая добавление комментария на сайте. """
    print('Добавляем комментарий')


delete_site()
add_comment()
