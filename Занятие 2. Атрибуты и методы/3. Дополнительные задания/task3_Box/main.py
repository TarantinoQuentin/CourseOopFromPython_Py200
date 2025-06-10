class Box:
    def __init__(self):
        self.items = []
        self.len = 0

    def __contains__(self, item):
        print("Вызов Box.__contains__")
        return item in self.items

    def __iter__(self):
        print("Вызов Box.__iter__")
        return iter(self.items)

    def __len__(self):
        print("Вызов Box.__len__")
        return self.len

    def __repr__(self):
        return f"Box({self.items})"

    def __add__(self, item):
        print("Вызов Box.__add__")
        if item not in self.items:
            self.items.append(item)
            self.len += 1
        return self

    def __getitem__(self, index):
        print("Вызов Box.__getitem__")
        return self.items[index]

    def __setitem__(self, index, value):
        print("Вызов Box.__setitem__")
        if value not in self.items:
            self.items[index] = value
        else:
            print(f"Элемент '{value}' уже существует в коллекции и не может быть добавлен повторно.")

    def __delitem__(self, index):
        print("Вызов Box.__delitem__")
        del self.items[index]


if __name__ == "__main__":
    box = Box()

    print(f"{'Добавляем элементы в коробку':-^40}")
    box += "apple"
    box += "banana"
    box += "orange"
    box += "apple"  # Дубликаты не добавляются
    print(box)  # Box(['apple', 'banana', 'orange'])
    # Проверяем количество элементов в коробке
    print(f"Количество элементов в коробке: {len(box)}")  # 3

    print(f"{'Проверка наличия элемента':-^40}")
    if "banana" in box:
        print("Банан есть в коробке\n")

    print(f"{'Итерация по элементам коробки':-^40}")
    for item in box:
        print(item)
    print()

    print(f"{'Обращение по индексу':-^40}")
    print(f"Элемент на позиции 1: {box[1]}\n")  # banana

    print(f"{'Установка значения по индексу':-^40}")
    box[1] = "grape"
    print(box)  # Box(['apple', 'grape', 'orange'])
    print()

    print(f"{'Попытка установки дубликата':-^40}")
    box[1] = "orange"  # Элемент уже существует в коллекции и не может быть добавлен повторно.
    print(box)  # Box(['apple', 'grape', 'orange'])
    print()

    print(f"{'Удаление элемента по индексу':-^40}")
    del box[1]
    print(box)  # Box(['apple', 'orange'])

    # Проверка количества элементов после удаления
    print(f"Количество элементов в коробке: {len(box)}")  # 2
