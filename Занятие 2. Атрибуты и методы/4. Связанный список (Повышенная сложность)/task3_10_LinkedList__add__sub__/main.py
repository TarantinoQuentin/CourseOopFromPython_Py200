from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0  # Добавили атрибут хранящий число узлов в связанном списке
        self.head: Optional[Node] = None

        if data is not None:
            self.extend(data)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """
        Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел.
        :param index:
        :return:
        """

        if not isinstance(index, int):
            raise TypeError('Индекс должен быть целым')

        if not 0 <= index < self.len:
            raise IndexError('Выход за допустимые границы')

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def append(self, value: Any) -> None:
        """
        Добавляет новый узел в конец списка.
        :param value: Значение для нового узла.
        """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1  # Индекс последнего узла
            last_node = self.step_by_step_on_nodes(last_index)  # Получаем последний узел

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Добавляет несколько новых узлов в конец списка из итерируемого объекта.
        :param iterable: Итерируемый объект с элементами для добавления.
        """
        for item in iterable:
            self.append(item)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def __repr__(self) -> str:
        """Возвращает строковое представление всего связанного списка."""
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current))
            current = current.next
        return f"LinkedList({' -> '.join(nodes)})"

    def __len__(self):
        print(f"Вызов метода __len__")
        return self.len

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        print(f"Вызов метода __getitem__, запросили index={index}")
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __iter__(self):
        """Инициализирует итератор и возвращает его."""
        print("Вызов метода __iter__")
        self.current_node = self.head
        return self

    def __next__(self):
        """Возвращает следующий элемент при итерации."""
        print("Вызов метода __next__")
        if self.current_node is None:  # Если больше нет элементов
            raise StopIteration
        current_value = self.current_node.value  # Получаем значение текущего узла
        self.current_node = self.current_node.next  # Переходим на следующий узел
        return current_value

    def __add__(self, other: Any) -> 'LinkedList':
        """
        Метод добавляет либо отдельный узел (Node), либо другой связанный список (LinkedList)
        в конец текущего связного списка.
        """
        print(f"Вызов метода __add__, запросили добавление other={other}")
        # TODO реализуйте метод

    def __sub__(self, node: Node) -> 'LinkedList':
        """
        Метод удаляет указанный узел (Node) из связанного списка, если он существует.
        """
        print(f"Вызов метода __sub__, запросили удаление node={node}")
        # TODO реализуйте метод


if __name__ == "__main__":
    # Создаем исходный связанный список
    ll = LinkedList([1, 2, 3])
    print("Исходный список:", ll)

    # Тестируем __add__ с Node
    ll = ll + Node(4)
    print("После добавления Node(4):", ll)  # LinkedList(1 -> 2 -> 3 -> 4)

    # Тестируем __add__ с LinkedList
    ll2 = LinkedList([5, 6])
    ll = ll + ll2
    print("После добавления LinkedList([5, 6]):", ll)  # LinkedList(1 -> 2 -> 3 -> 4 -> 5 -> 6)

    # Тестируем __sub__
    ll = ll - Node(3)
    print("После удаления Node(3):", ll)  # LinkedList(1 -> 2 -> 4 -> 5 -> 6)

    try:
        ll = ll - Node(10)  # Попытка удалить несуществующий узел
    except ValueError:
        print("Ожидаемая ошибка")
