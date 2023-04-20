def search_and_output_years_with_triple_digits(year_one, year_two):
    for year in range(year_one, year_two + 1):
        flag = False

        for digit in range(10):
            count = 0
            year_temp = year
            while year_temp > 0:
                if year_temp % 10 == digit:
                    count += 1
                year_temp //= 10
            if count >= 3:
                flag = True
                break

        if flag:
            print(year)


user_year_one = int(input('Введите первый год: '))
user_year_two = int(input('Введите второй год: '))

print(f'\nГоды от {user_year_one} до {user_year_two} с тремя одинаковыми цифрами:')
search_and_output_years_with_triple_digits(user_year_one, user_year_two)
