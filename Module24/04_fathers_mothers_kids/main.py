class Parent:
    def __init__(self):
        print('\n---Добавляем родителя---')
        parent_name = input('Введите имя родителя: ')
        while True:
            try:
                parent_age = int(input('Введите возраст родителя: '))
                break
            except ValueError:
                print('Возраст должен быть целым числом!')

        self.name = parent_name
        self.age = parent_age
        self.children = []

    def info(self):
        children_names = []
        for child in self.children:
            children_names.append(child.name)

        print('\nИмя родителя: {}\nВозраст родителя: {}\nДети родителя: {}'.format(
            self.name, self.age, children_names
        ))

    def add_child(self):
        print('\n---Добавляем ребёнка---')
        child_name = input('Введите имя ребёнка: ')

        while True:
            try:
                child_age = int(input('Введите возраст ребёнка: '))
                if (self.age - child_age) > 16:
                    break
                print('Возраст ребёнка должен быть меньше возраста родителя хотя бы на 16 лет!\n')
            except ValueError:
                print('Возраст должен быть целым числом!')

        print('Состояния спокойствия ребёнка:', Child.calm_states)
        while True:
            try:
                child_calm_state = int(input('Введите состояние спокойствия ребёнка цифрой 0, 1, 2 или 3: '))
                if child_calm_state in Child.calm_states:
                    break
            except ValueError:
                print('Некорректный ввод! Введите цифру 0, 1, 2 или 3.')

        print('Состояния голода ребёнка:', Child.hunger_states)
        while True:
            try:
                child_hunger_state = int(input('Введите состояние голода ребёнка цифрой 0, 1 или 2: '))
                if child_hunger_state in Child.hunger_states:
                    break
            except ValueError:
                print('Некорректный ввод! Введите цифру 0, 1 или 2.')

        self.children.append(Child(child_name, child_age, child_calm_state, child_hunger_state))

    def is_children_hungry(self):
        for child in self.children:
            if child.hunger_state > 0:
                return False
        return True

    def feed_children(self):
        print('\n---Кормим детей---')
        for child in self.children:
            if child.hunger_state == 0:
                print(f'Ваш ребёнок {child.name} не хочет кушать, он сытый.')
            else:
                child.hunger_state -= 1
                print('Ваш ребёнок {} покормлен. Теперь он {}.'.format(
                    child.name, Child.hunger_states[child.hunger_state]
                ))

    def is_children_calm(self):
        for child in self.children:
            if child.calm_state > 0:
                return False
        return True

    def calm_children(self):
        print('\n---Успокаиваем детей---')
        for child in self.children:
            if child.calm_state == 0:
                print(f'Ваш ребёнок {child.name} и так спокойный, его не нужно успокаивать.')
            else:
                child.calm_state -= 1
                print('Ваш ребёнок {} стал спокойнее. Сейчас он {}.'.format(
                    child.name, Child.calm_states[child.calm_state]
                ))


class Child:
    calm_states = {0: 'спокойный', 1: 'раздраженный', 2: 'агрессивный', 3: 'неуправляемый'}
    hunger_states = {0: 'сытый', 1: 'слегка голодный', 2: 'голодный'}

    def __init__(self, name, age, calm_state, hunger_state):
        self.name = name
        self.age = age
        self.calm_state = calm_state
        self.hunger_state = hunger_state


parent_1 = Parent()
parent_1.info()

parent_1.add_child()
parent_1.add_child()
parent_1.info()

while True:
    if not parent_1.is_children_calm():
        print('\nНекоторых Ваших детей нужно успокоить!', end='')
        parent_1.calm_children()
    else:
        print('\nВсе дети сейчас спокойные.')
        break

while True:
    if not parent_1.is_children_hungry():
        print('\nНекоторых Ваших детей нужно покормить!', end='')
        parent_1.feed_children()
    else:
        print('\nВсе дети сейчас сытые.')
        break
