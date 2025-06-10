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

        # TODO установить значение следующего узла с помощью метода set_next

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        """
        Проверяет корректность узла.
        :param node: Узел для проверки
        :raises TypeError: Если узел некорректного типа
        """
        ...  # TODO реализуйте проверку корректности связываемого узла

    def set_next(self, next_: Optional["Node"] = None) -> None:
        """
        Устанавливает следующий узел, проверяя его корректность.
        :param next_: Следующий узел или None
        """
        # TODO метод должен проверить корректность узла (метод is_valid) и установить значение атрибуту next


if __name__ == '__main__':
    # TODO инициализируйте узел first_node со значением 1 и second_node со значением 2

    # TODO свяжите первый узел со вторым

    print(first_node)  # Node(1, Node(2, None))
    print(second_node)  # Node(2, None)

    try:
        Node(3, 2)
    except TypeError:
        print("Верно")  # Верно
    else:
        print("Неверно")

