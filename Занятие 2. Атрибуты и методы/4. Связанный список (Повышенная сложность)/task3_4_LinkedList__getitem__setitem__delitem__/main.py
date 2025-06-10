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
        ...  # TODO верините атрибут длины

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        print(f"Вызов метода __getitem__, запросили index={index}")
        node = ...  # TODO получите узел при помощи метода step_by_step_on_nodes по требуемому индексу
        ...  # TODO верните значение узла

    def __setitem__(self, key: int, value: Any):
        """ Метод устанавливает значение узла по указанному индексу. """
        print(f"Вызов метода __setitem__, запросили изменение на позиции key={key} со значением value={value}")
        node = ...  # TODO получите узел при помощи метода step_by_step_on_nodes по требуемому индексу
        ...  # TODO в атрибут value объекта node установите новое значение

    def __delitem__(self, key: int):
        """ Метод удаляет значение узла по указанному индексу. В качестве следующего элемента
        ставится тот, что был за удаляемым.
        """
        print(f"Вызов метода __delitem__, запросили удаление на позиции key={key}")
        if key == 0:
            # Удаление первого узла
            self.head = ...  # TODO установите значение ссылки на следующий элемент
        else:
            # Поиск предыдущего узла
            previous_node = ...  # TODO найдите предыдущий узел (предыдущий относительно key)
            # Удаление текущего узла и связывание предыдущего с последующим
            current_node = ...  # TODO получите значение текущего узла через предыдущий
            # Следующий узел определяется относительно текущего
            next_node = current_node.next if current_node else None
            ...  # TODO свяжите предыдущий узел (previous_node) и следующий (next_node)  используя linked_nodes

        ...  # TODO обновите значение длины после удаления


if __name__ == '__main__':
    linked_list = LinkedList([1, 2, 3, 4])

    # Используем __getitem__ для получения значения узла
    print(linked_list[2])

    # Используем __setitem__ для изменения значения узла
    linked_list[2] = 10
    print(linked_list)

    # Используем __delitem__ для удаления узла
    del linked_list[1]
    print(linked_list)
    print(len(linked_list))

    del linked_list[2]
    print(linked_list)

    del linked_list[0]
    print(linked_list)
