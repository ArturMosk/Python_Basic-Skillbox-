def create_and_output_synonyms_pairs(number):
    synonyms_pairs = dict()
    for i_pair in range(1, number + 1):
        print(f'{i_pair}-я пара: ', end='')
        pair = input()
        pairs = pair.split()
        synonyms_pairs[pairs[0]] = pairs[-1]

    return synonyms_pairs


def search_word_and_print_synonym(word):
    is_flag = False
    for syn1, syn2 in synonyms.items():
        if word == syn1.lower():
            print('Синоним:', syn2)
            is_flag = True
            return is_flag
        elif word == syn2.lower():
            print('Синоним:', syn1)
            is_flag = True
            return is_flag
    print('Такого слова в словаре нет.')

    return is_flag


pairs_amt = int(input('Введите количество пар слов: '))
synonyms = create_and_output_synonyms_pairs(pairs_amt)
print()

while True:
    user_word = input('Введите слово: ').lower()
    synonym_searched = search_word_and_print_synonym(user_word)
    if synonym_searched:
        break
