import random


class House:
    """
    Базовый класс, описывающий жилище семьи.
    """

    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0


class Person:
    """
    Базовый класс, описывающий человека - члена семьи.

    Args:
        name (str): передаётся имя члена семьи
        house (class): передаётся объект проживания члена семьи

    Attributes:
        __total_eat_food (int): счетчик общего кол-ва съеденной членами семьи еды
    """

    __total_eat_food = 0

    def __init__(self, name, house):
        self.name = name
        self.satiation = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return f'Человек {self.name}'

    def get_total_eat_food():
        """
        Геттер для получения текущего значения общего кол-ва съеденной членами семьи еды

        :return Person.__total_eat_food
        :rtype: int
        """
        return Person.__total_eat_food

    def set_total_eat_food(self, eat_food_amount):
        """
        Сеттер для установления значения общего кол-ва съеденной членами семьи еды

        :param eat_food_amount: кол-во еды, съеденное одним из членов семьи
        :rtype: int
        """
        Person.__total_eat_food += eat_food_amount

    def info(self):
        """
        Метод info(), выдающий на экран текущие значения.
        Сытости, Степени счастья, Еды в холодильнике, Еды для кота, Денег в тумбочке, Грязи в доме.
        """
        print('Сытость: {}\n'
              'Степень счастья: {}\n'
              'Еда в холодильнике: {}\n'
              'Еда для кота: {}\n'
              'Деньги в тумбочке: {}\n'
              'Грязь в доме: {}'.format(
            self.satiation,
            self.happiness,
            self.house.food,
            self.house.cat_food,
            self.house.money,
            self.house.dirt
        ))

    def eat(self):
        """
        Метод eat(), реализующий алгоритм принятия пищи членом семьи.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}'.format('Совершено действие: покушать. '), end='')
        appetite = random.randint(1, 30)
        if appetite > self.house.food:
            self.satiation += self.house.food
            self.set_total_eat_food(self.house.food)
            print('{}\033[0m'.format(f'Съедено {self.house.food} единиц еды.'))
            self.house.food = 0
        else:
            self.satiation += appetite
            self.set_total_eat_food(appetite)
            print('{}\033[0m'.format(f'Съедено {appetite} единиц еды.'))
            self.house.food -= appetite

    def petting_the_cat(self):
        """
        Метод petting_the_cat(), реализующий алгоритм "погладить кота" членом семьи.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: погладить кота.'))
        self.happiness += 5
        self.satiation -= 10

    def is_too_bad_fed(self):
        """
        Метод is_too_bad_fed(), оценивающий степень сытости члена семьи.

        :return True: степень сытости ниже критического значения
        :rtype bool

        :return False: степень сытости выше критического значения
        :rtype bool
        """
        if self.satiation < 0:
            return True
        return False

    def is_depressed(self):
        """
        Метод is_depressed(), оценивающий степень счастья члена семьи.

        :return True: степень счастья ниже критического значения
        :rtype bool

        :return False: степень счастья выше критического значения
        :rtype bool
        """
        if self.happiness < 10:
            return True
        return False


class Husband(Person):
    """
    Класс Husband. Родитель: Person. Описывает Мужа.

    Attributes:
        __earn_money (int): счётчик общего кол-ва заработанных денег.
    """

    __earn_money = 0

    def __str__(self):
        return f'Муж {self.name}'

    def get_earn_money(self):
        """
        Геттер для получения текущего значения общего кол-ва заработанных денег.

        :return self.__earn_money
        :rtype: int
        """
        return self.__earn_money

    def work(self):
        """
        Метод work(), реализующий алгоритм работы Мужа для заработка денег.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: сходить на работу.'))
        self.house.money += 150
        self.satiation -= 10
        Husband.__earn_money += 150

    def play(self):
        """
        Метод play(), реализующий алгоритм роста степени счастья Мужа от игры в компьютер.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: поиграть.'))
        self.happiness += 20
        self.satiation -= 10


class Wife(Person):
    """
    Класс Wife. Родитель: Person. Описывает Жену.

    Attributes:
        __total_buy_fur_coat (int): счётчик общего кол-ва купленных шуб.
    """
    __total_buy_fur_coat = 0

    def __str__(self):
        return f'Жена {self.name}'

    def get_total_buy_fur_coat(self):
        """
        Геттер для получения текущего значения общего кол-ва купленных шуб.

        :return self.__total_buy_fur_coat
        :rtype: int
        """
        return self.__total_buy_fur_coat

    def buy_food(self):
        """
        Метод buy_food(), реализующий алгоритм покупки Женой еды для членов семьи.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: купить еду в холодильник.'))
        if self.house.money > 200:
            self.house.food += 200
            self.house.money -= 200
        else:
            self.house.food += (self.house.money // 10) * 10
            self.house.money = self.house.money % 10

        self.satiation -= 10

    def buy_cat_food(self):
        """
        Метод buy_cat_food(), реализующий алгоритм покупки Женой еды для домашних животных.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: купить еду для кота.'))
        if self.house.money > 200:
            self.house.cat_food += 200
            self.house.money -= 200
        else:
            self.house.cat_food += (self.house.money // 10) * 10
            self.house.money = self.house.money % 10

        self.satiation -= 10

    def buy_fur_coat(self):
        """
        Метод buy_fur_coat(), реализующий алгоритм покупки Женой шубы.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: купить шубу.'))
        self.house.money -= 350
        self.happiness += 60
        self.satiation -= 10
        Wife.__total_buy_fur_coat += 1

    def cleaning_the_house(self):
        """
        Метод cleaning_the_house(), реализующий алгоритм уборки Женой грязи в доме.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: уборка в доме.'))
        if self.house.dirt > 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0

        self.satiation -= 10


class Child(Person):
    """
    Класс Child. Родитель: Person. Описывает Ребёнка.
    """

    def __str__(self):
        return f'Ребёнок {self.name}'

    def play(self):
        """
        Метод play(), реализующий алгоритм повышения уровня счастья Ребёнка во время игр.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: поиграть.'))
        self.happiness += 20
        self.house.dirt += 5
        self.satiation -= 10

    def sleep(self):
        """
        Метод sleep(), реализующий алгоритм сна Ребёнка.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: поспать.'))
        self.satiation -= 10

    def do_homework(self):
        """
        Метод do_homework(), реализующий алгоритм выполнения Ребёнком домашнего задания.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: делать уроки.'))
        self.happiness -= 10
        self.satiation -= 10


class Cat:
    """
    Базовый класс, описывающий Кота.

    Args:
        name (str): передаётся кличка кота
        house (class): передаётся объект проживания кота

    Attributes:
        __total_eat_cat_food (int): счетчик общего кол-ва съеденной котами еды
    """
    __total_eat_cat_food = 0

    def __init__(self, name, house):
        self.name = name
        self.satiation = 30
        self.house = house

    def __str__(self):
        return f'Кот {self.name}'

    def get_total_eat_cat_food():
        """
        Геттер для получения текущего значения общего кол-ва съеденной котом кошачьей еды.

        :return Cat.__total_eat_cat_food
        :rtype: int
        """
        return Cat.__total_eat_cat_food

    def set_total_eat_cat_food(self, eat_cat_food_amount):
        """
        Сеттер для установления значения общего кол-ва съеденной кошачьей еды.

        :param eat_cat_food_amount: кол-во кошачьей еды, съеденное одним котом.
        :rtype: int
        """
        Cat.__total_eat_cat_food += eat_cat_food_amount

    def info(self):
        """
        Метод info(), выдающий на экран текущие значения
        Сытости, Еды для кота, Грязи в доме.
        """
        print('Сытость: {}\n'
              'Еда для кота: {}\n'
              'Грязь в доме: {}'.format(
            self.satiation,
            self.house.cat_food,
            self.house.dirt
        ))

    def eat(self):
        """
        Метод eat(), реализующий алгоритм принятия пищи котом.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}'.format('Совершено действие: покушать. '), end='')
        appetite = random.randint(1, 10)
        if appetite > self.house.cat_food:
            self.satiation += self.house.cat_food * 2
            self.set_total_eat_cat_food(self.house.cat_food)
            print('{}\033[0m'.format(f'Съедено {self.house.cat_food} единиц еды.'))
            self.house.cat_food = 0
        else:
            self.satiation += appetite * 2
            self.set_total_eat_cat_food(appetite)
            print('{}\033[0m'.format(f'Съедено {appetite} единиц еды.'))
            self.house.cat_food -= appetite

    def sleep(self):
        """
        Метод sleep(), реализующий алгоритм сна кота.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: поспать.'))
        self.satiation -= 10

    def tear_up_the_wallpaper(self):
        """
        Метод tear_up_the_wallpaper(), реализующий алгоритм, когда кот дерёт обои.
        """
        print('\033[33m{}\033[0m'.format(self.__str__()))
        print('\033[32m{}\033[0m'.format('Совершено действие: драть обои.'))
        self.house.dirt += 5
        self.satiation -= 10

    def is_too_bad_fed(self):
        """
        Метод is_too_bad_fed(), оценивающий степень сытости кота.

        :return True: степень сытости ниже критического значения
        :rtype bool

        :return False: степень сытости выше критического значения
        :rtype bool
        """

        if self.satiation < 0:
            return True
        return False


def actions_for_pets():
    """
    Алгоритм жизни домашних животных (котов) в семье по приоритетам.

    :return True: кот жив, поскольку его степень сытости выше критического значения.
    :rtype bool

    :return False: кот умер, поскольку его степень сытости ниже критического значения.
    :rtype bool
    """
    for pet in pets:
        print()
        number = random.randint(1, 2)
        if (pet.satiation < 20) and (pet.house.cat_food > 0):
            pet.eat()
        elif number == 1:
            pet.tear_up_the_wallpaper()
        else:
            pet.sleep()
        pet.info()

        if pet.is_too_bad_fed():
            print(f'\n!!! К сожалению, {pet.name} умер от голода.')
            return False
    return True


def actions_for_husband():
    """
    Алгоритм жизни Мужа в семье по приоритетам.

    :return True: муж жив, поскольку его степень сытости и степень счастья выше критического значения.
    :rtype bool

    :return False: муж умер, поскольку его степень сытости или степень счастья ниже критического значения.
    :rtype bool
    """
    print()
    if (husband.satiation < 20) and (husband.house.food > 0):
        husband.eat()
    elif husband.house.money < 100:
        husband.work()
    elif husband.happiness < 20:
        husband.petting_the_cat()
    elif (husband.happiness < 100) and (husband.house.money > 2000):
        husband.play()
    else:
        husband.work()
    husband.info()

    if husband.is_too_bad_fed():
        print(f'\n!!!К сожалению, {husband.name} умер от голода.')
        return False

    if husband.is_depressed():
        print(f'\n!!!К сожалению, {husband.name} умер от депрессии.')
        return False
    return True


def actions_for_wife():
    """
    Алгоритм жизни Жены в семье по приоритетам.

    :return True: жена жива, поскольку её степень сытости и степень счастья выше критического значения.
    :rtype bool

    :return False: жена умерла, поскольку её степень сытости или степень счастья ниже критического значения.
    :rtype bool
    """
    print()
    if (wife.satiation < 20) and (wife.house.food > 0):
        wife.eat()
    elif (wife.happiness < 60) and (wife.house.money > 2000):
        wife.buy_fur_coat()
    elif (wife.house.food < 50) and (wife.house.money > 0):
        wife.buy_food()
    elif (wife.house.cat_food < 50) and (wife.house.money > 0):
        wife.buy_cat_food()
    elif wife.house.dirt > 90:
        wife.cleaning_the_house()
    else:
        wife.petting_the_cat()
    wife.info()

    if wife.is_too_bad_fed():
        print(f'\n!!! К сожалению, {wife.name} умерла от голода.')
        return False

    if wife.is_depressed():
        print(f'\n!!! К сожалению, {wife.name} умерла от депрессии.')
        return False
    return True


def actions_for_child():
    """
    Алгоритм жизни Ребёнка в семье по приоритетам.

    :return True: ребёнок жив, поскольку его степень сытости и степень счастья выше критического значения.
    :rtype bool

    :return False: ребёнок умер, поскольку его степень сытости или степень счастья ниже критического значения.
    :rtype bool
    """
    number = random.randint(1, 4)
    print()
    if (child.satiation < 20) and (child.house.food > 0):
        child.eat()
    elif number == 1 or number == 2:
        child.do_homework()
    elif number == 3:
        child.play()
    else:
        child.petting_the_cat()
    child.info()

    if child.is_too_bad_fed():
        print(f'\n!!! К сожалению, {child} умер от голода.')
        return False

    if child.is_depressed():
        print(f'\n!!! К сожалению, {child} умер от депрессии.')
        return False
    return True


our_house = House()
husband = Husband('Иван', our_house)
wife = Wife('Марья', our_house)
child = Child('Игорь', our_house)
cat_1 = Cat('Мурзик', our_house)
cat_2 = Cat('Пушок', our_house)
cat_3 = Cat('Барсик', our_house)

pets = [cat_1, cat_2, cat_3]

is_flag = True
for index in range(1, 366):
    print('\033[31m{}\033[0m'.format(f'---- День {index}-й ----'))

    if our_house.dirt > 90:
        husband.happiness -= 10
        wife.happiness -= 10

    is_flag = actions_for_husband()  # Действия для Мужа
    if is_flag:
        is_flag = actions_for_wife()  # Действия для Жены
    if is_flag:
        is_flag = actions_for_child()  # Действия для Ребёнка
    if is_flag:
        is_flag = actions_for_pets()  # Действия для домашних животных

    if not is_flag:
        print('\nВы не смогли прожить весь год без потерь. Попробуйте что-то изменить...')
        break

    our_house.dirt += 5
    print()

print('\033[31m{}\033[0m'.format(f'---- Статистика прожитых дней ----'))
print(f'Муж заработал денег: {husband.get_earn_money()}.')
print(f'Было съедено единиц еды из холодильника: {Person.get_total_eat_food()}.')
print(f'Было съедено единиц кошачьей еды: {Cat.get_total_eat_cat_food()}.')
print(f'Жена купила шуб: {wife.get_total_buy_fur_coat()}.')
