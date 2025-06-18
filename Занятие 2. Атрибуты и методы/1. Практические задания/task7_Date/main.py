class Date:
    def __init__(self, day: int, month: int, year: int):
        if not isinstance(day, int):
            raise TypeError('День должен быть целочисленным значением')
        self.day = day
        if not isinstance(month, int):
            raise TypeError('Месяц должен быть целочисленным значением')
        self.month = month
        if not isinstance(year, int):
            raise TypeError('Год должен быть целочисленным значением')
        self.year = year

    def __str__(self) -> str:
        return f'{self.day:0>2}/{self.month:0>2}/{self.year}'

    def __repr__(self) -> str:
        return f'Date(day={self.day}, month={self.month}, year={self.year})'

if __name__ == "__main__":
    date1 = Date(1, 1, 2021)
    print(date1)  # 01/01/2021
    date2 = Date(11, 10, 1999)
    print(date2)  # 11/10/1999
    print(repr(date1), repr(date2))  # Date(day=1, month=1, year=2021) Date(day=11, month=10, year=1999)

    try:
        Date('1', 1, 2021)
    except TypeError:
        print('Верный вызов TypeError')  # Верный вызов TypeError
    else:
        print('Должен быть вызов TypeError')
