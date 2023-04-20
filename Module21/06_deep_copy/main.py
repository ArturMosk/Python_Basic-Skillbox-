import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def create_site_for_new_product(data, product):
    data['html']['head']['title'] = f'Куплю/продам {product} недорого'
    data['html']['body']['h2'] = f'У нас самая низкая цена на {product}'

    return data


def print_new_site(data):
    for i_product, i_site in data.items():
        print(f'Сайт для {i_product}:')
        print("site = {")
        print("    'html': {")
        print("            'title': {}".format(i_site['html']['head']['title']))
        print("        },")
        print("        'body': {")
        print("            'h2': {}',".format(i_site['html']['body']['h2']))
        print("            'div': 'Купить',")
        print("            'p': 'Продать'")
        print("        }")
        print("    }")
        print("}")
        print()


sites_amt = int(input('Сколько сайтов: '))
new_sites = dict()
for _ in range(sites_amt):
    product_name = input('Введите название продукта для нового сайта: ')
    new_site = create_site_for_new_product(copy.deepcopy(site), product_name)
    new_sites[product_name] = new_site
    print_new_site(new_sites)
