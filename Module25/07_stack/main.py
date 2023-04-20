class Stack:
    """
    Класс, который реализует стек и его возможности (добавление и удаление элемента).
    """

    def __init__(self):
        self.elements = []

    def __str__(self):
        return f'{self.elements}'

    def add_element(self, new_element):
        """
        Метод, реализующий добавление нового элемента.

        :param new_element: добавляемый элемент
        :rtype any
        """
        self.elements.append(new_element)

    def del_element(self, target_element):
        if target_element in self.elements:
            for element in reversed(self.elements):
                if element != target_element:
                    self.elements.pop(-1)
                else:
                    self.elements.pop(-1)
                    break


class TaskManager:
    """
    Класс, который реализует Менеджер задач на основе стека.
    Все задачи должны быть отсортированы по приоритету: чем меньше число, тем выше задача.
    """

    def __init__(self):
        self.tasks = []

    def __str__(self):
        """
        Встроенный метод, выводящий текстовую информацию об объекте класса TaskManager.
        Производит форматирование вывода первоначальной информации.
        Задачи выводятся по приоритетам.

        :return пустая строка
        """
        print('\nРезультат:')
        tasks_priority_unique = set()
        for i_task in self.tasks:
            tasks_priority_unique.add(i_task[1])
        for priority_unique in tasks_priority_unique:
            tasks_for_priority_unique = []
            print('   ', priority_unique, end=' ')
            for i_task in self.tasks:
                if i_task[1] == priority_unique:
                    tasks_for_priority_unique.append(i_task[0])
            text = '; '.join(tasks_for_priority_unique)
            print(text)

        return ''

    def check_duplicates(self):
        """
        Метод, реализующий алгоритм проверки введенных задач на дубликаты.
        Отдельно выделяются одинаковые задачи с разными приоритетами.
        Все найденные дубликаты удаляются.
        """
        tasks_duplicates = []
        tasks_description_unique = []
        tasks_duplicates_different_priority = []

        descriptions_unique = {i_task[0].lower() for i_task in self.tasks}
        for description in descriptions_unique:
            for i_task in self.tasks[::]:
                if (i_task[0].lower() == description) and (i_task[0].lower() not in tasks_description_unique):
                    i_priority = i_task[1]
                    tasks_description_unique.append(i_task[0].lower())
                elif (i_task[0].lower() == description) and (i_task[0].lower() in tasks_description_unique):
                    if i_task[1] != i_priority:
                        tasks_duplicates_different_priority.append(i_task)
                        self.tasks.remove(i_task)
                    else:
                        tasks_duplicates.append(i_task)
                        self.tasks.remove(i_task)

        if len(tasks_duplicates) != 0:
            print('Были обнаружены дубликаты следующих задач:')
            for duplicate in tasks_duplicates:
                print(duplicate)
            print('Обнаруженные дубликаты удалены.\n')

        if len(tasks_duplicates_different_priority) != 0:
            print('Также были обнаружены дубликаты задач с разными приоритетами:')
            for duplicate in tasks_duplicates_different_priority:
                print(duplicate)
            print('Оставлена задача, добавленная первой. Остальные дубликаты удалены.')
            print('Проверьте текущий приоритет оставшихся задач. При необходимости измените приоритет этих задач.')

    def new_task(self, description, priority):
        """
        Метод, реализующий добавление новой задачи в Менеджер задач.

        :param description: описание задачи
        :rtype description: str

        :param priority: приоритет задачи
        :rtype priority: int
        """
        self.tasks.append((description, priority))

    def change_priority(self):
        """
        Метод, реализующий изменение приоритета задачи в Менеджере задач.

        :return True: при успешном изменении приоритета задачи.
        """
        while True:
            description = input('Введите задачу, у которой нужно поменять приоритет: ')
            tasks_descriptions = [i_task[0].lower() for i_task in self.tasks]
            if description.lower() in tasks_descriptions:
                for i_task in self.tasks[::]:
                    if i_task[0].lower() == description.lower():
                        print(f'Текущий приоритет этой задачи: {i_task[1]}')
                        new_priority = int(input('Введите новый приоритет: '))
                        self.tasks.append((i_task[0], new_priority))
                        self.tasks.remove(i_task)
                        return True
            else:
                print('Ошибка ввода! Такой задачи нет в списке задач. Попробуйте ещё раз...')

    def del_task(self):
        """
        Метод, реализующий удаление задачи из Менеджера задач.

        :return True: при успешном удалении задачи.
        """
        while True:
            description = input('Введите задачу, которую нужно удалить: ')
            descriptions_unique = {i_task[0].lower() for i_task in self.tasks}
            if description.lower() in descriptions_unique:
                for i_task in self.tasks:
                    if i_task[0].lower() == description.lower():
                        self.tasks.remove(i_task)
                        return True
            else:
                print('Ошибка ввода! Такой задачи нет в списке задач. Попробуйте ещё раз...')


# ---- Реализация стека (добавление и удаление элемента) ----
stack_1 = Stack()
print('\033[31m{}\033[0m'.format(f'---- Реализация стека (добавление и удаление элемента) ----'))
print('Текущее состояние элементов:')
print(stack_1)

print('\nДобавляем элементы...')
for index in range(1, 7):
    stack_1.add_element(index)
    print(stack_1)

print('\nУдаляем элемент 3.')
stack_1.del_element(3)
print('\nТекущее состояние элементов:')
print(stack_1)

# ---- Реализация Менеджера задач ----
print('\033[31m{}\033[0m'.format(f'\n---- Реализация Менеджера задач ----'))
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("Поесть", 2)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 1)
manager.new_task("сдать дз", 2)
manager.new_task("поестЬ", 1)
manager.new_task("поестЬ", 3)

print('Состояние задач по мере их добавления (Задача: Приоритет):')
for task in manager.tasks:
    print(f'    {task[0]}: {task[1]}')
print()

# ---- Реализация проверки задач на дубликаты ----
print('\033[33m{}\033[0m'.format(f'\n---- Реализация проверки задач на дубликаты ----'))
manager.check_duplicates()
print(manager)

# ---- Реализация изменения приоритета у задачи ----
print('\033[33m{}\033[0m'.format(f'\n---- Реализация изменения приоритета у задачи ----'))
manager.change_priority()
print(manager)

# ---- Реализация удаления задачи ----
print('\033[33m{}\033[0m'.format(f'\n---- Реализация удаления задачи ----'))
manager.del_task()
print(manager)
