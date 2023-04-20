import functools


def singleton(cls):
    """ Декоратор класса. Превращает класс в одноэлементный. """

    @functools.wraps(cls)
    def wrapper():
        if cls() is None:
            instance = cls()
            return instance
        else:
            return None

    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
