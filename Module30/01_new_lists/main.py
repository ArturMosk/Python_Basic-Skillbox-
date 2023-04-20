from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

# Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
# Из списка names берутся только те имена, в которых есть минимум пять букв.
# Из списка numbers берётся произведение всех чисел.

floats_modified: List[float] = list(map(lambda number: round(number ** 3, 3), floats))
print(floats_modified)

names_filtered: List[str] = list(filter(lambda name: len(name) >= 5, names))
print(names_filtered)

numbers_reduced: List[int] = [reduce((lambda element_one, element_two: element_one * element_two), numbers)]
print(numbers_reduced)
