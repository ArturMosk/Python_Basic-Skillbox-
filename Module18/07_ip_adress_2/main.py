ip_address = input('Введите IP: ')

ip_address_lst = ip_address.split('.')

if len(ip_address_lst) != 4:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    flag = True
    for element in ip_address_lst:
        if not element.isdigit():
            print(element, '- это не целое положительное число.')
            flag = False
            break
        elif int(element) > 255:
            print(element, 'превышает 255.')
            flag = False
            break
    if flag:
        print('IP-адрес корректен.')
