class Tree:
    def __init__(self, wood_spices: str, height: int) -> None:
        """
        Создание и подготовка к работе объекта "Дерево".

        :param wood_spices: Порода дерева.
        :param height: Высота дерева.
        :raise TypeError: Если неверный тип данных.
        :raise ValueError: Если неверное значение высоты дерева.

        Пример:
        >>> oak_tree = Tree('Oak', 5)
        """
        if not isinstance(wood_spices, str):
            raise TypeError('Название породы дерева должно быть str')
        self.wood_spices = wood_spices
        if not isinstance(height, int):
            raise TypeError('Высота дерева должна быть int')
        if height <= 0:
            raise ValueError('Высота дерева не должна быть нулем или отрицательной')
        self.height = height

    def water_the_tree(self) -> None:
        """
        Функция полива дерева, увеличивает рост.

        :return: Возвращает увеличенный рост на один метр.

        Пример:
        >>> oak_tree = Tree('Oak', 5)
        >>> oak_tree.water_the_tree()
        """
        self.height += 1

    def is_choppable(self) -> bool:
        """
        Функция проверяет можно ли срубить дерево.
        Если дерево 5 метров и выше, то можно рубить.

        :return: bool

        Пример:
        >>> oak_tree = Tree('Oak', 5)
        >>> oak_tree.is_choppable()
        True
        """
        if self.height >= 5:
            return True
        return False

    def chop_the_tree(self) -> int:
        """
        Функция рубит дерево и возвращает количество бревен, которые с него получатся (одно бревно — 5 метров).

        :return: Возвращает количество бревен или ошибку.
        :raise ValueError: Недостаточная высота дерева.

        Пример:
        >>> birch_tree = Tree('Birch', 3)
        >>> birch_tree.chop_the_tree()
        Traceback (most recent call last):
        ...
        ValueError: Высота дерева еще недостаточна, чтобы его срубить, оно должно быть от 5 метров
        """
        if not self.is_choppable():
            raise ValueError('Высота дерева еще недостаточна, чтобы его срубить, оно должно быть от 5 метров')
        else:
            timbers_count = self.height // 5
            return timbers_count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
