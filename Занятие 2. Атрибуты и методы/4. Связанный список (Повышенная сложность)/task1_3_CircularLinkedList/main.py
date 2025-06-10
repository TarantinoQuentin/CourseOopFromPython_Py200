"""
Пример циклического односвязного списка без использования классических структур Python таких как list
Просто запустить и ознакомиться с кодом
"""


class Node:
    def __init__(self, data):
        self.data = data  # Данные
        self.next = None  # Ссылка на следующий узел


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            # Если список пустой, новый узел становится головным и указывает сам на себя
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Последний узел указывает на head, замыкая список

    def print_list(self):
        if not self.head:
            return "Список пуст"

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # Если вернулись к началу, выходим из цикла
                break
        print("... (возвращаемся к началу)")


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)

    cll.print_list()  # 1 -> 2 -> 3 -> ... (возвращаемся к началу)
