import math


class Car:
    """
    Базовый класс, описывающий Автомобиль.

    Args:
        coordinate_x (float): координата Х местонахождения Автомобиля
        coordinate_y (float): координата Y местонахождения Автомобиля
        angle (float):  угол, описывающий направление движения
    """

    def __init__(self, coordinate_x, coordinate_y, angle):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.angle = angle

    def __str__(self):
        return 'Автомобиль'

    def info(self):
        """
        Метод info(), выдающий на экран текущие значения
        Координаты Х,
        Координаты Y,
        Направление движения (угол в градусах против часовой стрелки
        между вектором оси Х и вектором движения).
        """
        print('\033[31m{}\033[0m'.format(f'---- {self.__str__()}: текущее состояние ----'))
        print('Координата Х = {}\nКоордината Y = {}\n'
              'Направление движения (угол в градусах против часовой стрелки '
              'между вектором оси Х и вектором движения) L = {}'.format(
            self.coordinate_x,
            self.coordinate_y,
            self.angle
        ))

    def move(self):
        """
        Метод move(), реализующий алгоритм перемещения Автомобиля на заданное расстояние
        в заданном направлении.

        :return distance: расстояние, на которое перемещается Автомобиль.
        :rtype float
        """
        while True:
            try:
                distance = float(input(f'Введите расстояние в км, которое должен проехать {self.__str__()}: '))
                print()
                if distance < 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Некорректный ввод! Введите вещественное неотрицательное число.')

        if 0 <= self.angle <= 90:
            new_coordinate_x = self.coordinate_x + distance * math.cos(math.radians(self.angle))
            new_coordinate_y = self.coordinate_y + distance * math.sin(math.radians(self.angle))
            self.coordinate_x = round(new_coordinate_x, 2)
            self.coordinate_y = round(new_coordinate_y, 2)
        elif 90 < self.angle <= 180:
            new_coordinate_x = self.coordinate_x - distance * math.cos(math.radians(180 - self.angle))
            new_coordinate_y = self.coordinate_y + distance * math.sin(math.radians(180 - self.angle))
            self.coordinate_x = round(new_coordinate_x, 2)
            self.coordinate_y = round(new_coordinate_y, 2)
        elif 180 < self.angle <= 270:
            new_coordinate_x = self.coordinate_x - distance * math.cos(math.radians(self.angle - 180))
            new_coordinate_y = self.coordinate_y - distance * math.sin(math.radians(self.angle - 180))
            self.coordinate_x = round(new_coordinate_x, 2)
            self.coordinate_y = round(new_coordinate_y, 2)
        elif 270 < self.angle <= 360:
            new_coordinate_x = self.coordinate_x + distance * math.cos(math.radians(360 - self.angle))
            new_coordinate_y = self.coordinate_y - distance * math.sin(math.radians(360 - self.angle))
            self.coordinate_x = round(new_coordinate_x, 2)
            self.coordinate_y = round(new_coordinate_y, 2)

        return distance

    def change_angle(self):
        """
        Метод change_angle(), устанавливающий новый угол, описывающий направление движения.

        :return distance: расстояние, на которое перемещается Автомобиль,
        :rtype float
        """
        while True:
            try:
                new_angle = float(input(f'Введите новое направление движения (угол в градусах от 0 до 360): '))
                print()
                if 0 <= new_angle <= 360:
                    if new_angle == 360:
                        new_angle = 0
                    self.angle = new_angle
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Некорректный ввод! Введите число от 0 до 360.')


class Bus(Car):
    """
    Класс Bus. Родитель: Car. Описывает Автобус.

    passengers (int): поле, содержащее текущее количество пассажиров в Автобусе
    money (float): поле, содержащее текущее количество заработанных денег в Автобусе
    """

    def __init__(self, coordinate_x, coordinate_y, angle):
        super().__init__(coordinate_x, coordinate_y, angle)
        self.passengers = 0
        self.money = 0

    def __str__(self):
        return 'Автобус'

    def info(self):
        """
        Метод info(), дополнительно к родительским выдающий на экран текущие значения
        Количества пассажиров в Автобусе,
        Общего количества денег в Автобусе за совершённые поездки.
        """
        super().info()
        print('Кол-во пассажиров: {}\nКол-во полученных денег: {}'.format(
            self.passengers,
            self.money
        ))

    def move(self):
        """
        Метод move(), реализующий алгоритм перемещения Автобуса на заданное расстояние
        в заданном направлении.
        Дополнительно к родительскому методу рассчитывает количество заработанных денег
        за текущий рейс. И увеличивает на это значение поле money.
        """
        bus_trip_length = super().move()
        trip_money = bus_trip_length * 5 * self.passengers
        print('Стоимость поездки 5 руб/км')
        print('Поездка завершена. За этот рейс заработано денег:', trip_money)
        print()
        self.money += trip_money

    def get_on_the_bus(self):
        """
        Метод get_on_the_bus(), реализующий алгоритм посадки пассажиров в Автобус.
        """
        while True:
            try:
                passengers_amount = int(input(f'Сколько пассажиров вошло в автобус? '))
                print()
                if passengers_amount < 0:
                    raise ValueError
                else:
                    self.passengers += passengers_amount
                    break
            except ValueError:
                print('Некорректный ввод! Введите вещественное неотрицательное число.')

    def get_off_the_bus(self):
        """
        Метод get_on_the_bus(), реализующий алгоритм выхода пассажиров из Автобуса.
        """
        while True:
            try:
                passengers_amount = int(input(f'Сколько пассажиров вышло из автобуса? '))
                print()
                if passengers_amount < 0:
                    raise ValueError
                elif passengers_amount <= self.passengers:
                    self.passengers -= passengers_amount
                    break
                else:
                    print('Из автобуса не может выйти больше пассажиров, чем в нём находится!')
            except ValueError:
                print('Некорректный ввод! Введите вещественное неотрицательное число.')


def actions_for_car():
    """
    Функция actions_for_car(), задающая алгоритм действий с Автомобилем по выбору пользователя.
    """
    while True:
        try:
            print()
            print('     1 - задать расстояние')
            print('     2 - задать направление движения')
            print('     3 - перейти к Автобусу')
            user_choice = int(input(f'Выберите действие (1, 2 или 3): '))
            if user_choice == 1:
                print()
                car_1.move()
                car_1.info()
            elif user_choice == 2:
                print()
                car_1.change_angle()
                car_1.info()
            elif user_choice == 3:
                return None
            else:
                print('\nНекорректный ввод! Введите цифру 1, 2 или 3.')
        except ValueError:
            print('\nНекорректный ввод! Введите цифру 1, 2 или 3.')


def actions_for_bus():
    """
    Функция actions_for_bus(), задающая алгоритм действий с Автобусом по выбору пользователя.
    """
    while True:
        try:
            print()
            print('     1 - запустить автобус в рейс')
            print('     2 - задать направление движения')
            print('     3 - завершить поездки')
            user_choice = int(input(f'Выберите действие (1, 2 или 3): '))
            if user_choice == 1:
                print()
                bus_1.get_on_the_bus()
                bus_1.move()
                bus_1.get_off_the_bus()
                bus_1.info()
            elif user_choice == 2:
                print()
                bus_1.change_angle()
                bus_1.info()
            elif user_choice == 3:
                print('\nСчастливого пути!')
                return None
            else:
                print('\nНекорректный ввод! Введите цифру 1, 2 или 3.')
        except ValueError:
            print('\nНекорректный ввод! Введите цифру 1, 2 или 3.')


car_1 = Car(0, 0, 0)
bus_1 = Bus(0, 0, 0)

car_1.info()
actions_for_car()

print('\nТеперь Автобус!')
bus_1.info()
actions_for_bus()
