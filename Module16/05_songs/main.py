violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

user_number = int(input('Сколько песен выбрать? '))

time_total = 0
for index in range(user_number):
    print(f'Название {index + 1}-й песни:', end=' ')
    song_name = input()
    for song in violator_songs:
        if song[0] == song_name:
            time_total += song[1]

time_total = round(time_total, 2)
print('\nОбщее время звучания песен:', time_total, 'минуты')
