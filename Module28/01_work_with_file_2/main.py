class File:
    """
    Контекст-менеджер, реализующий работу с файлами.

    Args and attrs:
        filename (str): имя файла
        mode (str): режим чтения/записи
    """

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> 'File':
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            self.file = open(self.filename, 'w')
        finally:
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('example.txt', 'r') as file:
    for line in file:
        print(line, end='')

with File('example.txt', 'w') as file:
    file.write("Язык программирования Python\n")
    file.write(6)
    file.write("Язык программирования Java\n")
