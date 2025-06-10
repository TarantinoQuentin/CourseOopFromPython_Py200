import doctest


class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        >>> glass = Glass(-500, 0)  # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        ValueError: Объем стакана должен быть положительным числом
        >>> glass = Glass('500', 0)  # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        TypeError: Объем стакана должен быть типа int или float
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        True
        >>> glass = Glass(500, 100)
        >>> glass.is_empty_glass()
        False
        """
        if self.occupied_volume == 0:
            return True
        return False

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        >>> glass.occupied_volume
        200
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        if self.occupied_volume + water > self.capacity_volume:
            raise ValueError("Перелили жидкость")
        self.occupied_volume += water

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        """
        if not isinstance(estimate_water, (int, float)):
            raise TypeError("Объем извлекаемой жидкости должен быть типа int или float")
        if estimate_water < 0:
            raise ValueError("Объем извлекаемой жидкости должен положительным числом")
        if self.occupied_volume - estimate_water < 0:
            raise ValueError(f"Нельзя извлечь больше, чем есть, на текущий момент есть {self.occupied_volume}")
        self.occupied_volume -= estimate_water


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
