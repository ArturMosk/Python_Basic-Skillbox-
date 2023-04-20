text = input('Введите строку: ')

# text_lst = list(text)
# text_encrypted_lst = []
# symbol = text_lst[0]
# count = 0
# while len(text_lst) > 0:
#     if text_lst[0] == symbol:
#         count += 1
#     else:
#         element = symbol + str(count)
#         text_encrypted_lst.append(element)
#         symbol = text_lst[0]
#         count = 1
#     if len(text_lst) == 1:
#         element = symbol + str(count)
#         text_encrypted_lst.append(element)
#     text_lst.pop(0)

text_separated = []
sequence = text[0]
for index in range(1, len(text)):
    if text[index] == text[index - 1]:
        sequence += text[index]
    else:
        text_separated.append(sequence)
        sequence = text[index]
    if index == len(text) - 1:
        text_separated.append(sequence)

text_encrypted_lst = [(sequence[0] + str(len(sequence))) for sequence in text_separated]

text_encrypted = ''.join(text_encrypted_lst)
print('\nЗакодированная строка:', text_encrypted)
