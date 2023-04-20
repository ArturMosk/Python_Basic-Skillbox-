import random


class KillError(Exception):
    """
    Класс исключения KillError, влияющий на карму. Родитель: Exception.
    """
    pass


class DrunkError(Exception):
    """
    Класс исключения DrunkError, влияющий на карму. Родитель: Exception.
    """
    pass


class CarCrashError(Exception):
    """
    Класс исключения CarCrashError, влияющий на карму. Родитель: Exception.
    """
    pass


class GluttonyError(Exception):
    """
    Класс исключения GluttonyError, влияющий на карму. Родитель: Exception.
    """
    pass


class DepressionError(Exception):
    """
    Класс исключения DepressionError, влияющий на карму. Родитель: Exception.
    """
    pass


class Person:
    """
    Базовый класс Человек, у которого отслеживаем ежедневное изменение кармы.

    Attributes:
        human_fails (dict): исключения и их описания, влияющие на карму.
    """
    human_fails = {KillError: 'Вы совершили убийство невинного существа! Сегодня Ваша карма не увеличилась.\n',
                   CarCrashError: 'Вы совершили ДТП! Сегодня Ваша карма не увеличилась.\n',
                   DrunkError: 'Вы напились! Сегодня Ваша карма не увеличилась.\n',
                   GluttonyError: 'Вы обожрались. Сегодня Ваша карма не увеличилась.\n',
                   DepressionError: 'Вы впали в депрессию. Сегодня Ваша карма не увеличилась.\n'}

    def __init__(self):
        self.__karma = 0
        self.__day = 1

    def get_karma(self):
        """
        Геттер для получения текущего значения кармы
        :return __karma:
        :rtype: int
        """
        return self.__karma

    def one_day(self):
        """
        Функция one_day(), которая возвращает количество кармы от 1 до 7
        и может с вероятностью 1 к 10 выкинуть одно из исключений.

        :raise Exception: с вероятностью 1 к 10 возникает одно из исключений, карма не увеличивается,
        исключение записывается в файл.
        """
        daily_karma = random.randint(1, 7)
        day_fail_probability = random.randint(1, 10)
        print(f'Сегодня день {self.__day}-й')
        self.__day += 1
        fail_name = random.choice(list(self.human_fails))
        try:
            if day_fail_probability == 10:
                raise fail_name
            else:
                self.__karma += daily_karma
                print(f'Ваша карма увеличилась на {daily_karma}. Сейчас Ваша карма {self.__karma}.\n')
        except fail_name:
            fail_message = self.human_fails[fail_name]
            print(fail_message)
            write_log_file(f'День {self.__day}-й\n')
            write_log_file(fail_message)


def write_log_file(message):
    """
    Запись исключения в файл.

    :param message: сообщение, которое необходимо записать в файл.
    :rtype str
    """
    file.write(message)


person = Person()
with open('karma.log', 'w') as file:
    while person.get_karma() < 500:
        person.one_day()
        person.get_karma()

print('Хвала Всевышнему! Вы достигли просветления.')
