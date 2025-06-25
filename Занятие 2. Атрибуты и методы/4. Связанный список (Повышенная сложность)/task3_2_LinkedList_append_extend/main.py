from typing import Iterable, Optional, Any
from node import Node


class LinkedList:
    """Класс, который описывает односвязный список."""

    def __init__(self, data: Iterable = None):
        """Инициализирует пустой список."""
        self.head: Optional[Node] = None

        if data is not None:
            self.extend(data)

    def append(self, value: Any) -> None:
        """
        Добавляет новый узел в конец списка.
        :param value: Значение для нового узла.
        """
        append_node = Node(value)
        if self.head is None:
            # Если список пустой, новый узел становится головным
            self.head = append_node
        else:
            current = self.head
            # Проходим до последней известной ссылки
            while current.next is not None:
                current = current.next
            self.linked_nodes(current, append_node)  # Добавляем новый узел

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


if __name__ == "__main__":
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)

    # Создаем связанный список
    linked_list = LinkedList()
    print(linked_list)

    # Добавляем элементы в конец списка
    linked_list.append(1)
    linked_list.append(2)
    print(linked_list)

    # Добавляем несколько элементов с помощью extend
    linked_list.extend([3, 4, 5])
    print(linked_list)
