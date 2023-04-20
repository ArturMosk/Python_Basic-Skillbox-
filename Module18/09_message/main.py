def reverse_and_output_word(word):
    if word.isalpha():
        return word[::-1]

    word_reversed_lst = []
    i_start = 0
    for index in range(len(word)):
        if not word[index].isalpha():
            word_tmp = word[i_start: index]
            word_reversed_lst.append(word_tmp[::-1] + word[index])
            i_start = index + 1
        if index == len(word) - 1:
            word_tmp = word[i_start:]
            word_reversed_lst.append(word_tmp[::-1])
    word_reversed = ''.join(word_reversed_lst)

    return word_reversed


text = input('Сообщение: ')

text_lst = text.split()
text_reversed_lst = [(reverse_and_output_word(element)) for element in text_lst]
text_reversed = ' '.join(text_reversed_lst)

print('Новое сообщение:', text_reversed)
