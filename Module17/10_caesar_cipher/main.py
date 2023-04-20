def encrypt_and_print_text(text, shift):
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    text_lst = list(text)
    text_encrypt_lst = text_lst[:]
    for i_text in range(len(text_lst)):
        if text_lst[i_text] in alphabet:
            i_alphabet = alphabet.index(text_lst[i_text])
            if i_alphabet + shift > len(alphabet) - 1:
                i_encrypt = (i_alphabet + shift) - len(alphabet)
            else:
                i_encrypt = (i_alphabet + shift)

            text_encrypt_lst[i_text] = alphabet[i_encrypt]

    text_encrypt = ''
    for element in text_encrypt_lst:
        text_encrypt += element

    print('Зашифрованное сообщение:', text_encrypt)


user_text = input('Введите сообщение: ')
user_shift = int(input('Введите сдвиг: '))

encrypt_and_print_text(user_text, user_shift)
