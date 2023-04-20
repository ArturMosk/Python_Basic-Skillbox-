import math


def count_and_output_coordinates(number_x, number_y, radius):
    length_between_00_and_XY = math.sqrt(number_x ** 2 + number_y ** 2)
    if length_between_00_and_XY <= radius:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')


print('Введите координаты монетки:\n')
user_number_x = float(input('X: '))
user_number_y = float(input('Y: '))
user_radius = float(input('Введите радиус: '))

count_and_output_coordinates(user_number_x, user_number_y, user_radius)
