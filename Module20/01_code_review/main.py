def count_and_output_interests_and_surnames_length(data):
    full_interests = set()
    full_length_surnames = 0
    for id, parameters in data.items():
        full_interests.update(set(parameters.get('interests', [])))
        full_length_surnames += len(parameters.get('surname', ''))

    return full_interests, full_length_surnames


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

pairs = []
for id, parameters in students.items():
    pairs.append((id, parameters.get('age', None)))

print('Список пар "ID студента — возраст":', pairs)

students_interests, students_surnames_length = count_and_output_interests_and_surnames_length(students)
print('Полный список интересов всех студентов:', students_interests)
print('Общая длина всех фамилий студентов:', students_surnames_length)
