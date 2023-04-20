import random

team_one = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_two = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [team_one[index] if team_one[index] > team_two[index] else team_two[index] for index in range(20)]

print('Первая команда:', team_one)
print('Вторая команда:', team_two)
print('Победители тура:', winners)
