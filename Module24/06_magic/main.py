class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Ether):
            return AirElemental()


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Ether):
            return EarthElemental()


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Ether):
            return FireElemental()


class Water:
    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Ether):
            return WaterElemental()


class Ether:
    def __init__(self):
        self.name = 'Эфир'

    def __add__(self, other):
        if isinstance(other, Fire):
            return FireElemental()
        elif isinstance(other, Earth):
            return EarthElemental()
        elif isinstance(other, Air):
            return AirElemental()
        elif isinstance(other, Water):
            return WaterElemental()


class EarthElemental:
    def __init__(self):
        self.name = 'Земляной элементаль'


class WaterElemental:
    def __init__(self):
        self.name = 'Водяной элементаль'


class AirElemental:
    def __init__(self):
        self.name = 'Воздушный элементаль'


class FireElemental:
    def __init__(self):
        self.name = 'Огненный элементаль'


class Storm:
    def __init__(self):
        self.name = 'Шторм'


class Lightning:
    def __init__(self):
        self.name = 'Молния'


class Dust:
    def __init__(self):
        self.name = 'Пыль'


class Lava:
    def __init__(self):
        self.name = 'Лава'


class Dirt:
    def __init__(self):
        self.name = 'Грязь'


class Steam:
    def __init__(self):
        self.name = 'Пар'


def choose_and_output_number_element(number):
    print()
    while True:
        try:
            choice = int(input(f'Введите номер {number}-го базового элемента: '))
            if choice not in base_elements.keys():
                raise ValueError
            return choice
        except ValueError:
            print('Ошибка при вводе номера базового элемента!')


air_element = Air()
water_element = Water()
earth_element = Earth()
fire_element = Fire()
ether_element = Ether()
base_elements = {1: air_element, 2: water_element, 3: earth_element, 4: fire_element, 5: ether_element}

while True:
    print('Имеются базовые элементы:')
    for number, element in base_elements.items():
        print(f'{number} - {element.name}')

    print('Соединим любые два из перечисленных базовых элементов.')

    choice_1 = choose_and_output_number_element(1)
    choice_2 = choose_and_output_number_element(2)

    new_element = base_elements[choice_1] + base_elements[choice_2]
    if not new_element:
        print('\n{} и {} не смогли создать новый элемент!'.format(
            base_elements[choice_1].name, base_elements[choice_2].name
        ))
    else:
        print('\n{} и {} создали новый элемент - {}'.format(
            base_elements[choice_1].name, base_elements[choice_2].name, new_element.name
        ))

    print('Попробуйте ещё раз.\n')
