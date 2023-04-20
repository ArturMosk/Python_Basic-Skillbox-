class Property:
    """
    Базовый класс, описывающий имущество.

    Args:
        worth (int): передаётся стоимость имущества
    """

    def __init__(self, worth):
        self.__worth = worth
        self.__name = 'Собственность'
        self.__tax_divider = 1

    def set_name(self, own_name):
        """
        Сеттер для установления названия имущества

        :param own_name
        :rtype: str
        """
        self.__name = own_name

    def set_tax_divider(self, own_divider):
        """
        Сеттер для установления налога на имущество

        :param own_divider: знаменатель коэффициента налога на имущество,
                            определяемый как (1 / own_divider)
        :rtype: int
        """
        self.__tax_divider = own_divider

    def count_tax(self):
        """
        Расчёт налога на имущество

        :return tax
        :rtype float
        """
        tax = self.__worth / self.__tax_divider
        print(f'{self.__name} облагается налогом в {tax} рублей.')
        return tax


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property.

    Args:
        worth (int): передаётся стоимость Квартиры
    """

    def __init__(self, worth):
        super().__init__(worth)
        self.set_name('Квартира')
        self.set_tax_divider(1000)


class Car(Property):
    """
    Класс Машина. Родитель: Property.

    Args:
        worth (int): передаётся стоимость Машины
    """

    def __init__(self, worth):
        super().__init__(worth)
        self.set_name('Машина')
        self.set_tax_divider(200)


class CountryHouse(Property):
    """
    Класс Дача. Родитель: Property.

    Args:
        worth (int): передаётся стоимость Дачи
    """

    def __init__(self, worth):
        super().__init__(worth)
        self.set_name('Дача')
        self.set_tax_divider(500)


property = []

total_money = int(input('Введите количество Ваших денег: '))

flat_worth = int(input('Введите стоимость Вашей квартиры: '))
flat = Apartment(flat_worth)
property.append(flat)

car_worth = int(input('Введите стоимость Вашей машины: '))
car = Car(car_worth)
property.append(car)

countryhouse_worth = int(input('Введите стоимость Вашей дачи: '))
countryhouse = CountryHouse(countryhouse_worth)
property.append(countryhouse)

total_tax = 0
print()
for element in property:
    own_tax = element.count_tax()
    total_tax += own_tax

print(f'\nОбщая сумма налогов на Ваше имущество составляет {total_tax} рублей.')

difference = total_tax - total_money
if total_tax > total_money:
    print(f'Для выплаты налогов Вам не хватает {difference} рублей!')
else:
    print('Ваших денег хватает для выплаты налогов.')
