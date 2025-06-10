from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        self.next = None
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        """
        Проверяет корректность узла.
        :param node: Узел для проверки
        :raises TypeError: Если узел некорректного типа
        """
        if not isinstance(node, (Node, type(None))):
            raise TypeError(f"Некорректный тип узла: ожидался 'Node' или 'None', получен {type(node).__name__}")

    def set_next(self, next_: Optional["Node"] = None) -> None:
        """
        Устанавливает следующий узел, проверяя его корректность.
        :param next_: Следующий узел или None
        """
        self.is_valid(next_)
        self.next = next_


def linked_nodes(left_node: Node, right_node: Optional["Node"] = None) -> None:
    """
    Функция, которая связывает между собой два узла.

    :param left_node: Левый или предыдущий узел
    :param right_node: Правый или следующий узел
    """
    # TODO реализовать функцию (в левую ноду устанавливаем ссылку через соответствующий метод)


if __name__ == '__main__':
    first_node = Node(1)
    second_node = Node(2)

    # TODO связать между собой два узла с помощью функции linked_nodes

    print(first_node)
    print(second_node)
