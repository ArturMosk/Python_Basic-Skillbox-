import random


class Warrior:
    def __init__(self, name):
        self.health = 100
        self.name = name

    def damage(self):
        self.health -= 20
        if self.health > 0:
            print(f'{self.name} имеет {self.health} единиц здоровья.\n')
        else:
            print(f'{self.name} убит!\n')


warrior_1 = Warrior('Воин Света')
warrior_2 = Warrior('Воин Тьмы')

while True:
    warriors = [warrior_1, warrior_2]

    winner = random.choice(warriors)
    warriors.remove(winner)
    looser = warriors[0]

    print(f'{winner.name} наносит удар.')
    looser.damage()
    if looser.health == 0:
        print(f'Победил {winner.name}!')
        break
