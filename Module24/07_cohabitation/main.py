import random


class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiation = 50
        self.house = house

    def info(self):
        print('Сытость {}-а: {}\nЕда в холодильнике: {}\nДеньги в тумбочке: {}\n'.format(
            self.name, self.satiation, self.house.food, self.house.money
        ))

    def eat(self):
        print(f'-{self.name} покушал.-')
        self.satiation += 10
        self.house.food -= 10

    def work(self):
        print(f'-{self.name} поработал.-')
        self.satiation -= 10
        self.house.money += 10

    def play(self):
        print(f'-{self.name} поиграл.-')
        self.satiation -= 10

    def buy_food(self):
        print(f'-{self.name} сходил в магазин за едой.-')
        self.house.money -= 10
        self.house.food += 10

    def is_well_fed(self):
        if self.satiation < 0:
            return False
        return True


class House:
    food = 50
    money = 0


our_house = House()
person_1 = Person('Bob', our_house)
person_2 = Person('John', our_house)
residents = [person_1, person_2]

for index in range(1, 366):
    print(f'---День {index}-й---')
    for person in residents:
        number = random.randint(1, 6)
        if (person.satiation < 20) and (person.house.food >= 10):
            person.eat()
        elif (person.house.food < 10) and (person.house.money >= 10):
            person.buy_food()
        elif person.house.money < 50:
            person.work()
        elif number == 1:
            person.work()
        elif number == 2 and (person.house.food >= 10):
            person.eat()
        else:
            person.play()

        person.info()

        if not person.is_well_fed():
            print(f'К сожалению, {person.name} умер от голода.')
            residents.remove(person)

    if len(residents) == 0:
        break
    print()
