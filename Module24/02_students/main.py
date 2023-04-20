import random


class Student:
    def __init__(self):
        self.surname_name = 'CommonName'
        self.group_number = 'CommonGroup'
        self.progress = list()

    def info(self):
        print('Фамилия и имя студента: {}\nГруппа: {}\nУспеваемость: {}\n'.format(
            self.surname_name, self.group_number, self.progress
        ))


class StudentsState:
    def __init__(self, amount):
        self.students = [Student() for _ in range(1, amount + 1)]

    def add_data(self):
        for student in self.students:
            student.surname_name = input('\nВведите фамилию и имя студента: ')
            student.group_number = input('Введите номер учебной группы студента: ')
            student.progress = [random.randint(1, 5) for _ in range(5)]

    def print_students_by_rating(self):
        students_rating = dict()
        print('\n--- Список студентов по возрастанию среднего балла ---\n')
        for student in self.students:
            rating = sum(student.progress) / len(student.progress)
            students_rating[rating] = student

        for rating in sorted(studens_rating.keys()):
            print('Средний балл:', rating)
            students_rating[rating].info()


our_students = StudentsState(10)
our_students.add_data()
our_students.print_students_by_rating()
