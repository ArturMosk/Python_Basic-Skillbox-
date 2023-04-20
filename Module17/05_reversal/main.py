def search_and_output_index_h(text):
    index = 1
    for symbol in text:
        if symbol == 'h':
            break
        index += 1

    return index


user_text = input('Введите строку: ')
index_h_start = search_and_output_index_h(user_text)
index_h_stop = search_and_output_index_h(user_text[::-1])
text_between_h = user_text[index_h_start: -index_h_stop]

print('Развёрнутая последовательность между первым и последним h:', text_between_h[::-1])
