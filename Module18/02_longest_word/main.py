text = input('Введите строку: ')

text_lst = text.lower().split()
length_max = 0
element_max = text_lst[0]

for element in text_lst:
    if len(element) > length_max:
        length_max = len(element)
        element_max = element

print('Самое длинное слово:', element_max)
print('Длина этого слова:', length_max)
