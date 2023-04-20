class Potato:
    potato_states = {0: 'Посажена', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.potato_state = 0

    def grow(self):
        if self.potato_state < 3:
            self.potato_state += 1

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, self.potato_states[self.potato_state]
        ))

    def is_ripe(self):
        if self.potato_state == 3:
            return True
        return False


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает...')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all(potato.is_ripe() for potato in self.potatoes):
            print('\nКартошка ещё не созрела!')
            print('Для успешного роста картошки нужен уход садовника!')
            return False
        else:
            print('\nВся картошка созрела! Можно собирать.')
            return True

    def print_all_states(self):
        print('\n---Состояние грядки---')
        for potato in self.potatoes:
            potato.print_state()


class TheGardener:
    def __init__(self, name, object):
        self.name = name
        self.object = object

    def care_of_garden(self):
        print(f'\nСадовник {self.name} поухаживал за картошкой на грядке.')
        self.object.grow_all()
        self.object.print_all_states()

    def collect_crop(self):
        print('\nСадовник {} собрал с грядки урожай картошки: {} штук.'.format(
            self.name, len(self.object.potatoes)
        ))
        self.object.potatoes = []
        print(f'Теперь грядка пустая ({len(self.object.potatoes)} штук) и можно сажать новую картошку.')


while True:
    try:
        potatoes_amt = int(input('\nСколько штук картошки будем сажать? '))
        if potatoes_amt < 1:
            raise ValueError

        garden_bed = PotatoGarden(potatoes_amt)
        garden_bed.print_all_states()
        result = garden_bed.are_all_ripe()

        gardener_name = input('Введите имя садовника: ')
        gardener_1 = TheGardener(gardener_name, garden_bed)

        while not result:
            gardener_1.care_of_garden()
            result = garden_bed.are_all_ripe()

        gardener_1.collect_crop()
    except ValueError:
        print('Ошибка ввода! Введите целое положительное число больше нуля.')
