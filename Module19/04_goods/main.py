def count_and_output_quantity_and_price(storage, code):
    amount_total = 0
    sum_total = 0
    for element in storage[code]:
        amount_total += element['quantity']
        sum_total += element['quantity'] * element['price']

    return amount_total, sum_total


def search_and_output_ending(number, index):
    if (number % 100 > 10) and (number % 100 < 19):
        ending = endings[0][index]
    else:
        i_ending = number % 10
        ending = endings[i_ending][index]

    return ending


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

endings = {
    0: ['штук', 'рублей'],
    1: ['штука', 'рубль'],
    2: ['штуки', 'рубля'],
    3: ['штуки', 'рубля'],
    4: ['штуки', 'рубля'],
    5: ['штук', 'рублей'],
    6: ['штук', 'рублей'],
    7: ['штук', 'рублей'],
    8: ['штук', 'рублей'],
    9: ['штук', 'рублей']
}

for product, code_name in goods.items():
    quantity_total, price_total = count_and_output_quantity_and_price(store, code_name)
    quantity_ending = search_and_output_ending(quantity_total, 0)
    price_ending = search_and_output_ending(price_total, 1)

    print(f'{product} — {quantity_total} {quantity_ending}, стоимость {price_total} {price_ending}')
