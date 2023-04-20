from typing import Any, Optional
from collections.abc import Iterable


class Node:
    """
    Класс, реализующий логику работы одного узла в односвязном списке (хранение данных и указателя).

    Args:
        data (Any): элемент односвязного списка
        next (Node): ссылка на следующий элемент односвязного списка
    """

    def __init__(self, data: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f'Node [{str(self.data)}]'


class LinkedList:
    """
    Класс-итератор, реализующий логику работы узлов в односвязном списке.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0
        self.counter = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.data)]
            while current.next is not None:
                current = current.next
                values.append(str(current.data))
            return f"[{' '.join(values)}]"
        return 'LinkedList []'

    def __iter__(self) -> Iterable[Any]:
        return self

    def __next__(self) -> int:
        self.counter += 1
        current_node = self.head
        if self.counter > self.length:
            raise StopIteration
        self.head = self.head.next

        return current_node.data

    def append(self, new_data: Any) -> None:
        """
        Метод, реализующий добавление элемента в конец списка.

        :param new_data: новый элемент списка
        :rtype Any

        :return: None
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.length += 1

    def get(self, index: int) -> Any:
        """
        Метод, реализующий получение элемента по индексу.

        :param index: индекс искомого элемента списка
        :rtype int

        :return: Any
        """
        current_node = self.head
        current_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        while current_index <= index:
            if current_index == index:
                return current_node.data
            current_index += 1
            current_node = current_node.next

    def remove(self, index: int) -> None:
        """
        Метод, реализующий удаление элемента по индексу.

        :param index: индекс искомого элемента списка
        :rtype int
        """
        current_node = self.head
        current_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if current_node is not None:
            if index == 0:
                self.head = current_node.next
                self.length -= 1
                return

        while current_node is not None:
            if current_index == index:
                break
            previous_node = current_node
            current_node = current_node.next
            current_index += 1

        previous_node.next = current_node.next
        self.length -= 1


print()
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

print('\nИтерация по списку с помощью цикла:')
for elem in my_list:
    print(elem)
