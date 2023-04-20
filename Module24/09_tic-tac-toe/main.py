class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    def __init__(self, index):
        self.is_free = True
        self.index = index
        self.cell_sign = str(index)


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.cells = [Cell(index) for index in range(1, 10)]

    def print_current_board(self):
        print('\nТекущее состояние доски:')
        print('-------------------')
        for index, cell in enumerate(self.cells):
            print('|  ', end='')
            if cell.cell_sign == 'X':
                print('\033[31m{}\033[0m'.format(cell.cell_sign), end='  ')
            elif cell.cell_sign == 'O':
                print('\033[34m{}\033[0m'.format(cell.cell_sign), end='  ')
            else:
                print(f'{cell.cell_sign}  ', end='')
            if (index + 1) % 3 == 0:
                print('|')
                print('-------------------')


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит

    def __init__(self, name, sign, board):
        self.name = name
        self.player_sign = sign
        self.board = board

    def is_cell_free(self, to_index):
        for cell in self.board.cells:
            if cell.index == to_index:
                if cell.is_free:
                    cell.cell_sign = self.player_sign
                    cell.is_free = False
                    return True
                else:
                    print('Ячейка, на которую Вы собираетесь пойти, занята! Выберите другую.')
                    return False

    def do_the_step(self):
        moves = [str(index) for index in range(1, 10)]
        while True:
            move = input(f'\n{self.name} делает ход. Введите номер ячейки: ')
            if move in moves:
                result = self.is_cell_free(int(move))
                if result:
                    return None
            else:
                print('Ошибка ввода! Попробуйте ещё раз.')


def is_end_of_game(player):
    win_combinations = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [1, 4, 7],
                        [2, 5, 8],
                        [3, 6, 9],
                        [1, 5, 9],
                        [3, 5, 7]]

    own_combination = [cell.index for cell in player.board.cells if cell.cell_sign == player.player_sign]

    for element in win_combinations:
        for digit in element:
            if digit not in own_combination:
                break
        else:
            print(f'\n!!! Игра окончена !!! Победил игрок {player.name}.')
            return True

    for cell in player.board.cells:
        if cell.is_free:
            break
    else:
        print('\nВсе ходы сделаны! Победителя нет. Ничья!')
        return True

    return False


gameboard = Board()
gameboard.print_current_board()

player_1_name = input('\nВведите имя игрока, делающего первый ход: ')
player_2_name = input('Введите имя второго игрока: ')
player_1 = Player(player_1_name, 'X', gameboard)
player_2 = Player(player_2_name, 'O', gameboard)

is_flag = True
while is_flag:
    for gameplayer in [player_1, player_2]:
        gameplayer.do_the_step()
        gameplayer.board.print_current_board()
        if is_end_of_game(gameplayer):
            is_flag = False
            break
        print('Продолжаем игру.')
