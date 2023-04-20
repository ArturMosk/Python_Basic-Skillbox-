def sort_incoming_list(user_list):
    for i_min in range(len(user_list)):
        for i_current in range(i_min, len(user_list)):
            if user_list[i_current] < user_list[i_min]:
                user_list[i_current], user_list[i_min] = user_list[i_min], user_list[i_current]

    return user_list


class_one = list(range(160, 177, 2))
class_two = list(range(162, 181, 3))

class_one.extend(class_two)
sorted_united_class = sort_incoming_list(class_one)

print('\nОтсортированный список учеников:', sorted_united_class)

# for index_i in range(len(class_two)):
#     flag = True
#     for index_j in range(len(class_one)):
#         if class_two[index_i] < class_one[index_j]:
#             class_one.insert(index_j, class_two[index_i])
#             flag = False
#             break
#     if flag:
#         class_one.append(class_two[index_i])