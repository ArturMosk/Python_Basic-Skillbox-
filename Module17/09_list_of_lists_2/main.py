nice_numbers = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

just_numbers = [element_k for element_i in nice_numbers for element_j in element_i for element_k in element_j]

print('Ответ:', just_numbers)
