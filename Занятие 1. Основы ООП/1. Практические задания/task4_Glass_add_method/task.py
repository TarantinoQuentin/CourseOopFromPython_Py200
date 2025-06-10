from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: int | float):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

    def init_occupied_volume(self, occupied_volume: int | float):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def add_water(self, volume: int | float):
        if not isinstance(volume, int | float):
            raise TypeError('Значение должно быть int или float')
        if volume < 0:
            raise ValueError('Значени должно быть больше нуля')
        if volume > (self.capacity_volume - self.occupied_volume):
            raise ValueError(f'Много, максимум можно добавить {self.capacity_volume - self.occupied_volume}')
        self.occupied_volume += volume

    def remove_water(self, volume: int | float):
        if not isinstance(volume, int | float):
            raise TypeError('Значение должно быть int или float')
        if volume < 0:
            raise ValueError('Значени должно быть больше нуля')
        if volume > self.occupied_volume:
            raise ValueError(f'Много, максимум можно вылить {self.occupied_volume}')
        self.occupied_volume -= volume


if __name__ == "__main__":
    glass = Glass(200, 100)

    glass.add_water(50)

    assert glass.occupied_volume == 150  # проверка правильности добавления воды
    print(glass.occupied_volume)

    glass.remove_water(100)

    assert glass.occupied_volume == 50  # проверка правильности отливания воды
    print(glass.occupied_volume)

    # Проверка неправильных сценариев
    try:
        glass.add_water('500')
    except TypeError as err:
        print(f"Ошибка {err!r} отрабатывается верно")
    else:
        print("Какую-то проверку в методе не учли")

    try:
        glass.add_water(500)
    except ValueError as err:
        print(f"Ошибка {err!r} отрабатывается верно")
    else:
        print("Какую-то проверку в методе не учли")

    try:
        glass.add_water(-50)
    except ValueError as err:
        print(f"Ошибка {err!r} отрабатывается верно")
    else:
        print("Какую-то проверку в методе не учли")

    try:
        glass.remove_water('500')
    except TypeError as err:
        print(f"Ошибка {err!r} отрабатывается верно")
    else:
        print("Какую-то проверку в методе не учли")

    try:
        glass.remove_water(500)
    except ValueError as err:
        print(f"Ошибка {err!r} отрабатывается верно")
    else:
        print("Какую-то проверку в методе не учли")

    try:
        glass.remove_water(-50)
    except ValueError as err:
        print(f"Ошибка {err!r} отрабатывается верно")
    else:
        print("Какую-то проверку в методе не учли")
