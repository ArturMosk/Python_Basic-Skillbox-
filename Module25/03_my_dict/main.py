class MyDict(dict):
    """
    Класс, который ведёт себя точно так же, как и обычный словарь. Родитель: dict
    """
    def get(self, key, default=0):
        """
        Метод по умолчанию возвращает не None, а число 0.

        :param key: ключ, по которому запрашивается значение словаря
        :param default: значение, которое выдаётся при отсутствии в словаре запрашиваемого ключа
        :return: результат метода get с переопределенным значением параметра default
        """
        return super().get(key, default)


books = {1: 'Три товарища',
         2: 'Каштанка',
         3: 'Маленький принц',
         4: 'Война и мир',
         5: 'Дуэль'}

my_dict = MyDict(books)
print(my_dict.get(6))