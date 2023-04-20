class Person:
    """
        Базовый класс, описывающий человека.

        Args:
            name (str): передаётся имя человека
            surname (str): передаётся фамилия человека
            age (int): передаётся возраст человека
        """

    def __init__(self, name, surname, age):
        self.set_name(name)
        self.set_surname(surname)
        self.set_age(age)

    def set_name(self, own_name):
        """
        Сеттер для установления имени человека

        :param own_name: имя
        :type own_name: str
        """
        self.__name = own_name

    def set_surname(self, own_surname):
        """
        Сеттер для установления фамилии человека

        :param own_surname: фамилия
        :type own_surname: str
        """
        self.__surname = own_surname

    def set_age(self, own_age):
        """
        Сеттер для установления возраста человека

        :param own_age: возраст
        :type own_age: int
        """
        self.__age = own_age

    def get_name(self):
        """
        Геттер для получения имени человека

        :return: __name
        :rtype: str
        """
        return self.__name

    def get_surname(self):
        """
        Геттер для получения фамилии человека

        :return: __surname
        :rtype: str
        """
        return self.__surname

    def get_age(self):
        """
        Геттер для получения возраста человека

        :return: __age
        :rtype: int
        """
        return self.__age


class Employee(Person):
    """
    Класс Работник. Родитель: Person.

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека

    Attributes:
        __position (str): Должность работника
    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.set_positiont('Работник')

    def __str__(self):
        info = '{} \033[34m{}\033[0m \033[34m{}\033[0m, ' \
               'возраст (в годах): \033[32m{}\033[0m, ' \
               'зарплата (в рублях): \033[33m{}\033[0m.'.format(
            self.get_position(),
            self.get_name(),
            self.get_surname(),
            self.get_age(),
            self.count_salary()
        )
        return info

    def set_positiont(self, own_position):
        """
        Сеттер для установления должности работника

        :param own_position: должность
        :type own_position: str
        """
        self.__position = own_position

    def get_position(self):
        """
        Геттер для получения позиции работника

        :return: __position
        :rtype: str
        """
        return self.__position

    def count_salary(self, salary):
        """
        Расчёт зарплаты работника

        :param salary: зарплата
        :type salary: int

        :return salary
        :rtype float
        """
        return salary


class Manager(Employee):
    """
    Класс Менеджер. Родитель: Employee.

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека

    Attributes:
        __position (str): Должность работника
    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.set_positiont('Менеджер')

    def count_salary(self, fixed_salary=13000):
        """
        Расчёт зарплаты менеджера

        :param fixed_salary: фиксированная зарплата
        :type fixed_salary: int

        :return fixed_salary: итоговая зарплата
        :rtype int
        """
        return fixed_salary


class Agent(Employee):
    """
    Класс Агент. Родитель: Employee.

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека

    Attributes:
        __position (str): Должность работника
        __sales_volume (int): Объём продаж в рублях
    """

    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.set_sales_volume(sales_volume)
        self.set_positiont('Агент')

    def set_sales_volume(self, own_sales_volume):
        """
        Сеттер для установления объёма продаж агента

        :param own_sales_volume: объём продаж
        :type own_sales_volume: int
        """
        self.__sales_volume = own_sales_volume

    def count_salary(self, wage=5000):
        """
        Расчёт зарплаты агента

        :param wage: фиксированный оклад
        :type wage: int

        :return salary: итоговая зарплата
        :rtype float
        """
        salary = wage + self.__sales_volume * 0.05
        return round(salary)


class Worker(Employee):
    """
    Класс Рабочий. Родитель: Employee.

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека

    Attributes:
        __position (str): Должность работника
        __hours_amt (int): Число отработанных часов
    """

    def __init__(self, name, surname, age, hours_amt):
        super().__init__(name, surname, age)
        self.set_hours_amt(hours_amt)
        self.set_positiont('Рабочий')

    def set_hours_amt(self, own_hours_amt):
        """
        Сеттер для установления числа отработанных часов рабочего

        :param own_hours_amt: число отработанных часов
        :type own_hours_amt: int
        """
        self.__hours_amt = own_hours_amt

    def count_salary(self, hour_rate=100):
        """
        Расчёт зарплаты рабочего

        :param hour_rate: ставка одного отработанного часа
        :type hour_rate: int

        :return salary: итоговая зарплата
        :rtype float
        """
        salary = hour_rate * self.__hours_amt
        return round(salary)


def get_and_output_age():
    """
    Запрос возраста работника, проверка введенного значения на допустимые величины.

    :return own_age: возраст работника
    :rtype int
    """
    while True:
        own_age = input('Введите возраст: ')
        if own_age.isdigit() and (int(own_age) in range(18, 90)):
            return int(own_age)
        else:
            print('Ошибка ввода! Возраст работника должен быть от 18 до 90 лет.')


def get_and_output_sales_volume():
    """
    Запрос объёма продаж для агента, проверка введенного значения на допустимые величины.

    :return own_sales_volume: объём продаж
    :rtype int
    """
    while True:
        own_sales_volume = input('Введите объём продаж: ')
        if own_sales_volume.isdigit() and int(own_sales_volume) >= 0:
            return int(own_sales_volume)
        else:
            print('Ошибка ввода! Объём продаж должен выражаться целым неотрицательным числом.')


def get_and_output_hours_amt():
    """
    Запрос числа отработанных часов для рабочего, проверка введенного значения на допустимые величины.

    :return own_hours_amt: число отработанных часов
    :rtype int
    """
    while True:
        own_hours_amt = input('Введите число отработанных часов: ')
        if own_hours_amt.isdigit() and int(own_hours_amt) >= 0:
            return int(own_hours_amt)
        else:
            print('Ошибка ввода! Число отработанных часов должно выражаться целым неотрицательным числом.')


def create_employee():
    """
    Запрос имени, фамилии и возраста для работника.

    :return user_name: имя работника
    :rtype str

    :return user_surname: фамилия работника
    :rtype str

    :return user_age: возраст работника
    :rtype int
    """
    user_name = input('Введите имя: ')
    user_surname = input('Введите фамилию: ')
    user_age = get_and_output_age()
    return user_name, user_surname, user_age


employees = []

print('\033[31m{}\033[0m'.format('---- Создаём трёх менеджеров ----'))
for index in range(1, 4):
    print(f'Менеджер № {index}')
    name, surname, age = create_employee()
    print()
    employees.append(Manager(name, surname, age))

print('\033[31m{}\033[0m'.format('---- Создаём трёх агентов ----'))
for index in range(1, 4):
    print(f'Агент № {index}')
    name, surname, age = create_employee()
    sales_volume = get_and_output_sales_volume()
    print()
    employees.append(Agent(name, surname, age, sales_volume))

print('\033[31m{}\033[0m'.format('---- Создаём трёх рабочих ----'))
for index in range(1, 4):
    print(f'Рабочий № {index}')
    name, surname, age = create_employee()
    hours_amt = get_and_output_hours_amt()
    print()
    employees.append(Worker(name, surname, age, hours_amt))

print('\033[31m{}\033[0m'.format('---- Сведения о сотрудниках ----'))
for element in employees:
    print(element)
