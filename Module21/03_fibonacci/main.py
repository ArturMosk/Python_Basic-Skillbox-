def Fibonachi(num):
    if num <= 2:
        result = 1
        return result
    result = Fibonachi(num - 1) + Fibonachi(num - 2)
    return result


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
number = Fibonachi(num_pos)
print('Число:', number)
