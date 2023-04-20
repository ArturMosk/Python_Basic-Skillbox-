violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_amount = int(input('Сколько песен выбрать? '))

numeric = ['первой', 'второй', 'третьей', 'четвёртой', 'пятой', 'шестой', 'седьмой', 'восьмой', 'девятой']
songs_time_total = 0

for i_song in range(songs_amount):
    print('Название {} песни: '.format(numeric[i_song]), end='')
    song_name = input()
    if song_name in violator_songs.keys():
        songs_time_total += violator_songs[song_name]
    else:
        print('Такой песни нет в нашем плейлисте!')

print('\nОбщее время звучания песен: {:.2f} минут'.format(songs_time_total))
