import random


class Card:
    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее
    def __init__(self, suit='', rank='', nominal=0):
        self.suit = suit
        self.rank = rank
        self.nominal = nominal


class Deck:
    #  Колода создаёт у себя объекты карт
    suits = ['пики', 'червы', 'трефы', 'бубны']
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}
    cards_for_play = []

    def __init__(self, decks_amt=1):
        for suit in self.suits:
            for i_rank, i_nominal in self.ranks.items():
                self.cards_for_play.append(Card(suit, i_rank, i_nominal))

        for _ in range(1, decks_amt):
            self.cards_for_play.extend(self.cards_for_play)

    def info(self):
        for element in self.cards_for_play:
            print(f'{element.rank} {element.suit}')


class Player:
    #  Игрок, у которого есть имя и какие-то карты на руках
    def __init__(self, name):
        self.name = name
        self.own_cards = []

    def get_card(self, amount=1):
        for _ in range(amount):
            element = random.choice(Deck.cards_for_play)
            self.own_cards.append(element)
            Deck.cards_for_play.remove(element)

    def cards_in_hand(self):
        for element in self.own_cards:
            print(f'{element.rank} {element.suit}')

    def score_in_hand(self):
        score_sum = 0
        for element in self.own_cards:
            if (score_sum + element.nominal > 21) and (element.rank == 'Туз'):
                score_sum += 1
            else:
                score_sum += element.nominal

        return score_sum


def choose_winner(player, diler):
    player_score = player.score_in_hand()
    diler_score = diler.score_in_hand()
    if player_score > diler_score:
        print(f'\n\n!!! Победителем является {player.name} с количеством очков {player_score} !!!')
    elif player_score == diler_score:
        print('\nУ дилера такое же количество очков.')
        diler.cards_in_hand()
        print('\nУ вас ничья! Вы остаётесь при своих.')
    else:
        print(f'\n\n!!! Победителем является {diler.name} с количеством очков {diler_score} !!!')
        diler.cards_in_hand()


deck_1 = Deck()
computer = Player('Дилер')
user_name = input('Введите имя игрока: ')
player_1 = Player(user_name)

player_1.get_card(2)
computer.get_card(2)
player_1_score = player_1.score_in_hand()
computer_score = computer.score_in_hand()

while player_1_score <= 21:
    print(f'\n{player_1.name}, у Вас в руке сейчас следующие карты:')
    player_1.cards_in_hand()
    player_1_score = player_1.score_in_hand()
    print('Сумма очков этих карт:', player_1_score)

    if player_1_score > 21:
        print('\nК сожалению, Ваше количество очков больше 21. Вы "сгораете"! Ваша ставка уходит к дилеру.')
    elif player_1_score == 21:
        choose_winner(player_1, computer)
        break
    elif player_1_score < 21:
        print('\nВаши дальнейшие действия: 1 - взять карту, 2 - остановиться')
        while True:
            action = input('Выберите действие (1 или 2): ')
            if action == '1' or action == '2':
                break
            print('Ошибка ввода! Введите цифру 1 или 2.')
        if action == '1':
            player_1.get_card()
        elif action == '2':
            choose_winner(player_1, computer)
            break
