text = input('Введите текст: ')

vowel_letters = 'аоуиеэяюыё'
vowel_text = [element for element in text if element in vowel_letters]

print('\nСписок гласных букв:', vowel_text)
print('Длина списка:', len(vowel_text))

