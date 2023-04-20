def create_and_output_orders(number):
    orders_total = []
    names = set()
    for i_order in range(1, number + 1):
        orders_by_name = dict()
        print(f'{i_order}-й заказ: ', end='')
        order = input()
        orders = order.split()
        orders_by_name[orders[0]] = [orders[1], int(orders[2])]
        orders_total.append(orders_by_name)
        names.add(orders[0])

    return orders_total, names


def search_and_output_orders_by_name(orders, names):
    orders_by_name = dict()
    for name in names:
        orders_for_name = dict()
        for element in orders:
            for buyer, order in element.items():
                if buyer == name:
                    if order[0] in orders_for_name:
                        orders_for_name[order[0]] += order[1]
                    else:
                        orders_for_name[order[0]] = order[1]
        orders_by_name[name] = orders_for_name

    return orders_by_name


def print_orders_by_name(orders_by_name):
    for name in sorted(orders_by_name.keys()):
        print(f'{name}:')
        for product in sorted(orders_by_name[name].keys()):
            print(' ' * (len(name) + 2), end='')
            print(f'{product}: {orders_by_name[name][product]}')


order_amt = int(input('Введите количество заказов: '))
buyers_orders, buyers_names = create_and_output_orders(order_amt)
orders_name = search_and_output_orders_by_name(buyers_orders, buyers_names)
print()
print_orders_by_name(orders_name)
