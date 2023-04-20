import math


class Ring:
    def __init__(self, coordinate_x=0, coordinate_y=0, radius=1):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius = radius

    def info(self):
        print('Координата центра круга X = {}\nКоордината центра круга Y = {}\nРадиус круга R = {}\n'.format(
            self.coordinate_x, self.coordinate_y, self.radius
        ))

    def find_and_output_square(self):
        square = math.pi * self.radius ** 2
        return square

    def find_and_output_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def ring_increase(self, number):
        square = math.pi * self.radius ** 2
        square_new = square * number
        radius_new = math.sqrt(square_new / math.pi)
        self.radius = radius_new

    def check_cross_another_ring(self, object):
        distance_min = self.radius + object.radius
        distance = math.sqrt((object.coordinate_x - self.coordinate_x) ** 2 +
                             (object.coordinate_y - self.coordinate_y) ** 2)
        if distance >= distance_min:
            print('Круги не пересекаются\n')
        else:
            print('Круги пересекаются\n')


ring_1 = Ring()
print('Параметры круга:')
ring_1.info()
ring_2 = Ring(4, 0, 2)
print('Параметры другого круга:')
ring_2.info()

square_1 = ring_1.find_and_output_square()
square_2 = ring_2.find_and_output_square()
print('Площадь круга равна:', square_1)
print('Площадь другого круга равна:', square_2, end='\n\n')

perimeter_1 = ring_1.find_and_output_perimeter()
perimeter_2 = ring_2.find_and_output_perimeter()
print('Периметр круга равен:', perimeter_1)
print('Периметр другого круга равен:', perimeter_2, end='\n\n')

ring_1.check_cross_another_ring(ring_2)

number_k = int(input('Увеличиваем круг в К раз. Введите К = '))
ring_1.ring_increase(number_k)
ring_1.info()

number_k = int(input('Увеличиваем другой круг в К раз. Введите К = '))
ring_2.ring_increase(number_k)
ring_2.info()

ring_1.check_cross_another_ring(ring_2)
