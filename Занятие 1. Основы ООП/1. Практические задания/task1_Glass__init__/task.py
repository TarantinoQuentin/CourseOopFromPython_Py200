from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        if not isinstance(capacity_volume, int | float):
            raise TypeError('Значение должно быть типа int или float')
        if capacity_volume <= 0:
            raise ValueError('Объем стакана должен быть больше 0')
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, int | float):
            raise TypeError('Значение должно быть типа int или float')
        if occupied_volume < 0 or occupied_volume > capacity_volume:
            raise ValueError('Заполненный объем не должен быть быть меньше 0 и больше объема стакана')
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    first_glass = Glass(10, 5)
    second_glass = Glass(200.05, 199.9)

    try:
        third_glass = Glass('200', 60)
        fourth_glass = Glass(100, 100.1)
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


