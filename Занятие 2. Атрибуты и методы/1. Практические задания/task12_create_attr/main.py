class Point2D:
    """
    Класс, который хранит координаты XY
    """
    def __init__(self, x: (int, float) = 0, y: (int, float) = 0):
        self.x = x
        self.y = y

    def add_new_attr_no_safe(self, attr: str, value: (int, float)):
        """
        Самописный метод добавляющий новый атрибут в объект. Данный подход нужно использовать осторожно,
        так как обходит некоторые важные механизмы. На практике лучше использовать функцию setattr
        :param attr: Именование (название) атрибута
        :param value: Значение
        :return:
        """
        # Как было сказано ранее, то если необходимо, то можно добавить атрибут непосредственно в словарь __dict__
        self.__dict__[attr] = value  # Так мы создали

    def add_new_attr_safe(self, attr: str, value: (int, float)):
        """
        Самописный метод добавляющий новый атрибут в объект через функцию setattr
        :param attr: Именование (название) атрибута
        :param value: Значение
        :return:
        """
        setattr(self, attr, value)  # Для добавления атрибутов рекомендуется использовать встроенную функцию setattr,
        # которая обеспечивает более безопасный и предсказуемый способ изменения атрибутов объекта.


class Point2DLock:
    """
    Класс, который хранит координаты XY, но благодаря __slots__ не позволяет добавить новых атрибутов из вне
    """
    __slots__ = ['x', 'y']

    def __init__(self, x: (int, float) = 0, y: (int, float) = 0):
        self.x = x
        self.y = y

    def add_new_attr_no_safe(self, attr: str, value: (int, float)):
        """
        Проверка взаимодействия __slots__ с __dict__
        """
        self.__dict__[attr] = value

    def add_new_attr_safe(self, attr: str, value: (int, float)):
        """
        Проверка взаимодействия __slots__ с setattr
        """
        setattr(self, attr, value)


if __name__ == "__main__":
    # Создание новых атрибутов через экземпляр
    point = Point2D(1, 1)
    print(point.x, point.y)
    point.z = 20
    print(point.x, point.y, point.z)

    # Создание новых атрибутов через setattr
    point = Point2D(1, 1)
    print(point.x, point.y)
    setattr(point, 'z', 20)
    print(point.x, point.y, point.z)

    # Создание новых атрибутов через небезопасный подход с __dict__
    point = Point2D(1, 1)
    print(point.x, point.y)
    point.add_new_attr_no_safe('z', 20)
    print(point.x, point.y, point.z)

    # Создание новых атрибутов через безопасный подход с __dict__ (setattr)
    point = Point2D(1, 1)
    print(point.x, point.y)
    point.add_new_attr_safe('z', 20)
    print(point.x, point.y, point.z)

    # Использование __slots__ и проверка возможности добавления элементов
    point = Point2DLock(1, 1)
    print(point.x, point.y)
    try:
        point.z = 20
    except AttributeError as err:
        print(f"При выполнении point.z = 20 получили ошибку: {err}")

    try:
        setattr(point, 'z', 20)
    except AttributeError as err:
        print(f"При выполнении setattr(point, 'z', 20) получили ошибку: {err}")

    try:
        point.add_new_attr_no_safe('z', 20)  #
    except AttributeError as err:
        print(f"При выполнении point.add_new_attr_no_safe('z', 20) получили ошибку: {err}")

    try:
        point.add_new_attr_safe('z', 20)
    except AttributeError as err:
        print(f"При выполнении point.add_new_attr_safe('z', 20) получили ошибку: {err}")









