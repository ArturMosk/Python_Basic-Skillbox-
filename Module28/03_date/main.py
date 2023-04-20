from datetime import datetime
from abc import ABC


class Date(ABC):
    """
    Абстрактный класс, реализующий конвертацию строки даты в объект класса Date,
    состоящий из соответствующих числовых значений дня, месяца и года.
    """

    @classmethod
    def from_string(cls, date_string: str) -> str:
        try:
            result = datetime.strptime(date_string, '%d-%m-%Y').date()
        except ValueError:
            return "Для конвертации в дату передаётся некорректная строка. " \
                   "Строка должна быть вида 'dd-mm-yyyy'\n"
        else:
            message = f'День: {result.day}	Месяц: {result.month}	Год: {result.year}'
            return message

    @classmethod
    def is_date_valid(cls, date_string: str) -> bool:
        try:
            datetime.strptime(date_string, '%d-%m-%Y').date()
        except ValueError:
            return False
        else:
            return True


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
