from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if not capacity_volume > 0:
            raise ValueError("Объем стакана должен быть больше 0")
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if occupied_volume < 0:
            raise ValueError("Не должно быть отрицательных значений")
        if occupied_volume > capacity_volume:
            raise ValueError("Налить в стакан больше того, что возможно нельзя")
        self.occupied_volume = occupied_volume  # объем жидкости в стакане


if __name__ == "__main__":
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.capacity_volume, glass1.occupied_volume)

    # TODO инициализировать ещё один стакан со значениями 200, 150
    glass2 = Glass(200, 150)
    # TODO  распечатать атрибут capacity_volume, occupied_volume экземпляра glass2
    print(glass2.capacity_volume, glass2.occupied_volume)

    print("Доливаем воды в первый стакан...")
    # TODO доливаем 50 единиц воды в первый стакан (за счет добавления значения к значению соответствующего атрибута)
    glass1.occupied_volume += 50

    print(glass1.capacity_volume, glass1.occupied_volume)
    print(glass2.capacity_volume, glass2.occupied_volume)

    assert glass1.capacity_volume == glass2.capacity_volume  # Проверяем, что объемы стаканов одинаковые (иначе будет ошибка)
    assert glass1.occupied_volume == glass2.occupied_volume  # Проверяем, что стаканы заполнены одинаково (иначе будет ошибка)

    print(id(glass1) is id(glass2))  # TODO сравнить id объектов (должно вернуть True или False)
