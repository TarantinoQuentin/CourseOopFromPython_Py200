class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.is_valid_date(day, month, year)

        self.day = day
        self.month = month
        self.year = year



    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        ...  # TODO Реализовать метод проверки високосного года

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...  # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году (учтите, что от високосного года меняется строка в DAY_OF_MONTH)

    def is_valid_date(self, day: int, month: int, year: int) -> bool:
        """Проверяет, является ли дата корректной"""
        ...  # TODO Проверить валидность даты, если дата невалидная вызвать ValueError, если валидная, то вернуть True

    def __str__(self):
        return f"{self.day:0>2}/{self.month:0>2}/{self.year:4}"


if __name__ == "__main__":
    date = Date(29, 2, 2000)
    print(date)  # 29/02/2000

    try:
        Date(29, 2, 2001)
    except ValueError:
        print("Верное поведение")  # Верное поведение
    else:
        print("Неверное поведение")


