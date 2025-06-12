class FloppyDisc:
    def __init__(self, memory_capacity: int|float, occupied_memory: int|float) -> None:
        """
        Создание и подготовка к работе объекта "Дискета".

        :param memory_capacity: Размер памяти нашей дискеты
        :param occupied_memory: Размер занятой памяти
        :raise TypeError: Если неверный тип данных
        :raise TypeError: Если объемы некорректных значений

        Примеры:
        >>> floppy_disc = FloppyDisc(1.44, 0)
        """
        self.limit = (0.36, 1.44)
        if not isinstance(memory_capacity, (int, float)):
            raise TypeError("Объем памяти должен быть типа int или float")
        if memory_capacity <= 0 or not (self.limit[0] <= memory_capacity <= self.limit[1]):
            raise ValueError("Объем памяти должен быть положительным числом и находиться в диапазоне от 0,36 до 1,44 мб.")
        self.memory_capacity = memory_capacity

        if not isinstance(occupied_memory, (int, float)):
            raise TypeError("Объем занятой памяти должен быть int или float")
        if 0 > occupied_memory > memory_capacity:
            raise ValueError("Объем занятой памяти не может быть отрицательным числом и должен находиться в диапазоне от 0,36 до 1,44 мб.")
        self.occupied_memory = occupied_memory

    def is_empty_disc(self) -> bool:
        """
        Функция проверяет является ли дискета пустой.

        :return: bool

        Пример:
        >>> floppy_disc = FloppyDisc(1.44, 0)
        >>> floppy_disc.is_empty_disc()
        True
        """
        if self.occupied_memory == 0:
            return True
        return False

    def write_data_to_disc(self, data_volume: int|float) -> None:
        """
        Запись данных на дискету.

        :param data_volume: Объем добавляемой информации.
        :raise TypeError: Неверный тип данных объема.
        :raise ValueError: Если объем некорректного значения.

        Примеры:
        >>> floppy_disc = FloppyDisc(1.44, 0)
        >>> floppy_disc.write_data_to_disc(200)
        Traceback (most recent call last):
        ...
        ValueError: Объем записываемой памяти не может быть отрицательным числом и не должен превышать объем дискеты
        """
        if not isinstance(data_volume, (int, float)):
            raise TypeError("Объем записываемой информации должен быть типа int или float")
        if data_volume < 0 or data_volume > self.memory_capacity:
            raise ValueError("Объем записываемой памяти не может быть отрицательным числом и не должен превышать объем дискеты")
        self.occupied_memory += data_volume

    def remove_data_from_disc(self, data_volume: int|float) -> None:
        """
        Удаляем данные с дискеты.

        :param data_volume: Объем удаляемой информации.
        :raise TypeError: Неверный тип данных объема.
        :raise ValueError: Если объем некорректного значения.

        Примеры:
        >>> floppy_disc = FloppyDisc(1.44, 1)
        >>> floppy_disc.remove_data_from_disc(1.01)
        Traceback (most recent call last):
        ...
        ValueError: Объем удаляемой информации не может быть отрицательным числом и не должен превышать объем записанных данных
        """
        if not isinstance(data_volume, (int, float)):
            raise TypeError("Объем удаляемой информации должен быть типа int или float")
        if data_volume < 0 or data_volume > self.occupied_memory:
            raise ValueError("Объем удаляемой информации не может быть отрицательным числом и не должен превышать объем записанных данных")
        self.occupied_memory -= data_volume


if __name__ == "__main__":
    import doctest
    doctest.testmod()
