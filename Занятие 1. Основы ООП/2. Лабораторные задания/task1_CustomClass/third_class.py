class ThisWork:
    def __init__(self, type: str, classes_to_do: int, completed_classes: int) -> None:
        """
        Создание и подготовка к работе объекта "Моя работа".

        :param type: Тип выполняемой работы.
        :param classes_to_do: Сколько требуется создать классов.
        :param completed_classes: Классов создано
        :raise TypeError: Неверный тип данных.

        Пример:
        >>> lab_work = ThisWork('lab', 1, 2)
        >>> another_lab_work = ThisWork('lab', '1', 2)
        Traceback (most recent call last):
        ...
        TypeError: Значение должно быть int
        """
        if not isinstance(type, str):
            raise TypeError('Называние работы должно быть str')
        self.type = type
        if not isinstance(classes_to_do, int):
            raise TypeError('Значение должно быть int')
        self.classes_to_do = classes_to_do
        if not isinstance(completed_classes, int):
            raise TypeError('Значение должно быть int')
        self.completed_classes = completed_classes

    def make_another_class(self, classes_done: int) -> None:
        """
        Создание классов, увеличивает параметр сделанных классов.

        :param classes_done: Сколько создал классов сейчас.
        :raise TypeError: Неверный тип данных количества созданных классов.

        Пример:
        >>> lab_work = ThisWork('lab', 1, 2)
        >>> lab_work.make_another_class('1')
        Traceback (most recent call last):
        ...
        TypeError: Количество добавленных классов должно быть int
        """
        if not isinstance(classes_done, int):
            raise TypeError('Количество добавленных классов должно быть int')
        self.completed_classes += classes_done

    def is_work_done(self) -> bool:
        """
        Проверка, выполнена ли работа.

        :return: Возвращает булевое значение.

        Пример:
        >>> lab_work = ThisWork('lab', 0, 1)
        >>> lab_work.is_work_done()
        True
        """
        if self.completed_classes >= self.classes_to_do:
            return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
