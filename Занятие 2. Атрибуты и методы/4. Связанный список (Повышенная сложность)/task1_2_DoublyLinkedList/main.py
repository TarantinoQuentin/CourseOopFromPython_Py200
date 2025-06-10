"""
Пример двусвязного списка без использования классических структур Python таких как list
Просто запустить и ознакомиться с кодом
"""


class Node:
    def __init__(self, data):
        self.data = data  # Данные
        self.next = None  # Ссылка на следующий узел
        self.prev = None  # Ссылка на предыдущий узел


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Если список пустой
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Ищем последний узел
                current = current.next
            current.next = new_node  # Ссылка предыдущего узла на новый узел
            new_node.prev = current  # Ссылка нового узла на предыдущий узел

    def print_list_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def print_list_backward(self):
        current = self.head
        if not current:  # Если список пустой
            return
        # Идём до конца списка
        while current.next:
            current = current.next
        # Проходим список в обратном порядке
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")


if __name__ == "__main__":
    # Пример использования
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    print("Прямой порядок:")
    dll.print_list_forward()  # 1 -> 2 -> 3 -> None

    print("Обратный порядок:")
    dll.print_list_backward()  # 3 -> 2 -> 1 -> None
