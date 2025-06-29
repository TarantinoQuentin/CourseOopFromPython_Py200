from datetime import date


class Room:
    """
    Базовый класс для номеров в отеле
    """
    def __init__(self, room_number: int, price_per_night: int):
        """
        Подготовка класса "Номер" к работе
        :param room_number: Номер (порядковый)
        :param price_per_night: Цена за ночь
        """
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__is_booked = False

    def book(self) -> None|Exception:
        """
        Метод для бронирования комнаты
        :raise: Возвращает ValueError, если номер уже забронирован
        :return: None
        """
        if not self.__is_booked:
            self.__is_booked = True
        else:
            raise ValueError(f'Номер {self.get_room_number()} {self.__class__.__name__} уже забронирован.')

    def unbook(self) -> None|Exception:
        """
        Метод для снятия брони с номера
        :raise: Возвращает ValueError, если номер еще не забронирован
        :return: None
        """
        if self.__is_booked:
            self.__is_booked = False
        else:
            raise ValueError(f'Номер {self.get_room_number()} {self.__class__.__name__} свободен.')

    def calculate_price(self, nights: int) -> int:
        """
        Метод для расчета стоимости проживания на протяжении указанных ночей
        :param nights: Количество ночей
        :return: Стоимость проживания
        """
        return self.__price_per_night * nights

    def get_room_number(self) -> int:
        """
        Метод возвращает номер
        :return: Номер
        """
        return self.__room_number

    def is_booked(self) -> bool:
        """
        Метод проверяет забронирован ли номер
        :return: bool
        """
        return self.__is_booked

    def __str__(self):
        return f'Номер {self.__room_number} {self.__class__.__name__}, {'забронирован' if self.is_booked else 'свободен'}, цена за ночь: {self.__price_per_night}.'

    def __repr__(self):
        result = f'{self.__class__.__name__}('
        for key, value in self.__dict__.items():
            result += f'{key}={value!r}, '
        return result[:-2] + ')'

class SingleRoom(Room):
    """
    Класс для одноместного номера
    """
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)


class DoubleRoom(Room):
    """
    Класс для двухместного номера
    """
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)


class Suite(Room):
    """
    Класс для люксового номера. Наценка 20%
    """
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)

    def calculate_price(self, nights: int) -> int|float:
        """
        Метод для расчета стоимости проживания на протяжении указанных ночей с наценкой за люксовый номер
        :param nights: Количество ночей
        :return: Стоимость проживания
        """
        price = super().calculate_price(nights)
        markup = price * 0.2
        return price + markup


class Booking:
    """
    Класс для управления бронированием
    """
    def __init__(self, room: Room|SingleRoom|DoubleRoom|Suite, check_in_date: date, check_out_date: date):
        """
        Подготовка класса "Управление бронированием" к работе
        :param room: Класс с номером
        :param check_in_date: Дата заезда
        :param check_out_date: Дата выезда
        """
        self.room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__nights = (check_out_date - check_in_date).days
        self.__total_price = self.room.calculate_price(self.__nights)


    def confirm_booking(self) -> None:
        """
        Метод бронирует номер и сообщает об успешном бронировании
        :return: None
        """
        self.room.book()
        print(f'Номер {self.room.get_room_number()} {self.room.__class__.__name__} успешно забронирован.')

    def cancel_booking(self) -> None:
        """
        Метод снимает бронь с номера и сообщает об успешном снятии
        :return: None
        """
        self.room.unbook()
        print(f'Бронь номера {self.room.get_room_number()} {self.room.__class__.__name__} успешно снята.')

    def __str__(self):
        if self.room.is_booked:
            book_status = 'забронирован'
            date_of_booking = f'{self.__check_in_date} — {self.__check_out_date} на {self.__nights} ночи'
            return f'Номер {self.room.get_room_number()} {self.room.__class__.__name__}, {book_status} {date_of_booking}, стоимость {self.__total_price}.'
        book_status = 'свободен'
        return f'Номер {self.room.get_room_number()} {self.room.__class__.__name__}, {book_status}, стоимость за ночь: {self.room.__price_per_night}.'

class Hotel:
    """
    Класс для управления отелем
    """
    def __init__(self, name: str):
        """
        Подготовка класса "Отель" к работе
        :param name: Название отеля
        """
        self._name = name
        self._rooms = []

    def add_room(self, room: Room|SingleRoom|DoubleRoom|Suite) -> None:
        """
        Метод добавляет номер в отель
        :param room: класс Room или его производные
        :return: None
        """
        self._rooms.append(room)

    def find_available_room(self) -> Room|SingleRoom|DoubleRoom|Suite|Exception:
        """
        Метод находит свободный номер
        :raise: ValueError, если нет свободных номеров
        :return: класс Room или его производные
        """
        for room in self._rooms:
            if not room.is_booked():
                return room
        raise ValueError('Свободных номеров нет.')

    def __str__(self):
        return f'Отель {self._name!r}, количество номеров: {len(self._rooms)}.'

if __name__ == "__main__":
    # Создаем отель
    hotel = Hotel("Grand Hotel")

    # Добавляем номера
    hotel.add_room(SingleRoom(101, 100))
    hotel.add_room(DoubleRoom(102, 150))
    hotel.add_room(Suite(103, 300))

    print(hotel)

    # Находим свободный номер и бронируем его
    room_to_book = hotel.find_available_room()
    booking = Booking(room_to_book, date(2024, 9, 1), date(2024, 9, 5))
    print(booking)

    # Подтверждаем бронирование
    booking.confirm_booking()

    # Пробуем снова забронировать ту же комнату
    try:
        booking2 = Booking(room_to_book, date(2024, 9, 10), date(2024, 9, 15))
        booking2.confirm_booking()
    except ValueError as e:
        print(e)

    # Отмена бронирования
    booking.cancel_booking()
