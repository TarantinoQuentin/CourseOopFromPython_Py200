from typing import Iterable, Optional, Any

from node import Node


class DoublyLinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0  # Добавили атрибут хранящий число узлов в связанном списке
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

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
            self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

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
        right_node.set_prev(left_node)

    def __repr__(self) -> str:
        """Возвращает строковое представление всего связанного списка."""
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current))
            current = current.next
        return f"DoublyLinkedList({' <-> '.join(nodes)})"

    def __len__(self):
        print(f"Вызов метода __len__")
        return self.len

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        print(f"Вызов метода __getitem__, запросили index={index}")
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, key: int, value: Any):
        """ Метод устанавливает значение узла по указанному индексу. """
        print(f"Вызов метода __setitem__, запросили изменение на позиции key={key} со значением value={value}")
        node = self.step_by_step_on_nodes(key)
        node.value = value

    def __delitem__(self, key: int):
        """ Метод удаляет значение узла по указанному индексу. В качестве следующего элемента
        ставится тот, что был за удаляемым.
        """
        print(f"Вызов метода __delitem__, запросили удаление на позиции key={key}")

        current = self.head
        if key == 0:
            # Удаление первого узла
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # Если список теперь пуст, сбрасываем tail
        elif key == self.len - 1:
            # Удаление последнего узла
            current = self.tail
            self.tail = current.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None  # Если список теперь пуст, сбрасываем head
        else:
            # Удаление узла из середины
            current_node = self.step_by_step_on_nodes(key)
            self.linked_nodes(current_node.prev, current_node.next)

        self.len -= 1

    def __contains__(self, value: Any) -> bool:
        """Метод для поддержки оператора in."""
        print(f"Вызов метода __contains__, запросили сравнение с value={value}")

        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

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

    # TODO добавьте метод __reversed__ из описания задачи


if __name__ == '__main__':
    list_ = [1, 2, 3, 4, 5]
    dll = DoublyLinkedList(list_)
    print(dll)

    print(list(reversed(dll)))
