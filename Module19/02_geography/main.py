def search_city_and_print_country(countries, city):
    is_flag = False
    for country, cities in countries.items():
        if city in cities:
            is_flag = True
            print(f'Город {city} расположен в стране {country}.')
            break

    if not is_flag:
        print(f'По городу {city} данных нет.')


countries_amt = int(input('Количество стран: '))

user_countries = dict()
for index in range(countries_amt):
    print(f'{index + 1}-я страна: ', end='')
    user_country = input()
    user_countries[user_country.split()[0]] = user_country.split()[1:]

for oder in ['Первый', 'Второй', 'Третий']:
    print()
    print(f'{oder} город: ', end='')
    user_city = input()
    search_city_and_print_country(user_countries, user_city)
