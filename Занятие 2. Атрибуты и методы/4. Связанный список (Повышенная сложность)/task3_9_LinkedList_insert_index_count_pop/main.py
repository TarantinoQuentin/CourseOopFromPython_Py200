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

    def insert(self, index: int, value: Any) -> None:
        """Вставляет новый узел с заданным значением в указанную позицию списка."""
        ...  # TODO реализуйте метод

    def index(self, value: Any) -> int:
        """Возвращает индекс первого узла со значением, равным value."""
        ...  # TODO реализуйте метод

    def count(self, value: Any) -> int:
        """Возвращает количество узлов со значением, равным value."""
        ...  # TODO реализуйте метод

    def pop(self, index: int = None) -> Any:
        """
        Удаляет и возвращает узел по указанному индексу.
        Если индекс не указан, удаляет и возвращает последний элемент.
        """
        ...  # TODO реализуйте метод


if __name__ == "__main__":
    ll = LinkedList([1, 2, 3, 4, 5])
    print("Исходный список:", ll)

    # Тестируем insert
    ll.insert(2, 10)
    print("После вставки 10 на индекс 2:", ll)  # LinkedList(1 -> 2 -> 10 -> 3 -> 4 -> 5)

    # Тестируем index
    idx = ll.index(10)
    print("Индекс элемента 10:", idx)  # 2

    # Тестируем count
    count_10 = ll.count(10)
    count_3 = ll.count(3)
    print("Количество элементов 10:", count_10)  # 1
    print("Количество элементов 3:", count_3)  # 1

    # Тестируем pop
    popped_value = ll.pop(2)
    print("После удаления элемента с индекса 2 (ожидаем 10):", popped_value)
    print("Список после pop:", ll)  # LinkedList(1 -> 2 -> 3 -> 4 -> 5)

    # Тестируем pop последнего элемента
    last_value = ll.pop()
    print("После удаления последнего элемента (ожидаем 5):", last_value)
    print("Список после удаления последнего элемента:", ll)  # LinkedList(1 -> 2 -> 3 -> 4)
