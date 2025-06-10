class Room:
    """
    Базовый класс для номеров в отеле
    """
    def __init__(self, room_number, price_per_night):
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__is_booked = False

    def book(self):
        if not self.__is_booked:
            self.__is_booked = True
            print(f"Комната {self.__room_number} успешно забронирована.")
        else:
            raise ValueError(f"Комната {self.__room_number} уже забронирована.")

    def unbook(self):
        if self.__is_booked:
            self.__is_booked = False
            print(f"Бронь с комнаты {self.__room_number} снята.")
        else:
            raise ValueError(f"Комната {self.__room_number} не была забронирована.")

    def calculate_price(self, nights):
        return self.__price_per_night * nights

    def get_room_number(self):
        return self.__room_number

    def is_booked(self):
        return self.__is_booked

    def __str__(self):
        status = "Забронирована" if self.__is_booked else "Свободна"
        return f"Комната {self.__room_number}: {status}, Цена: {self.__price_per_night} за ночь"


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
    Класс для люксового номера
    """
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)

    def calculate_price(self, nights):
        # Дополнительная наценка для люксовых номеров
        base_price = super().calculate_price(nights)
        luxury_tax = base_price * 0.2  # 20% надбавка
        return base_price + luxury_tax


class Booking:
    """
    Класс для управления бронированием
    """
    def __init__(self, room, check_in_date, check_out_date):
        if not isinstance(room, Room):
            raise TypeError("Номер должен быть объектом класса Room или его подкласса.")
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.nights = (check_out_date - check_in_date).days
        self.total_price = self.room.calculate_price(self.nights)

    def confirm_booking(self):
        self.room.book()
        print(f"Бронирование подтверждено с {self.check_in_date} по {self.check_out_date}.")
        print(f"Общая стоимость: {self.total_price}")

    def cancel_booking(self):
        self.room.unbook()
        print(f"Бронирование на комнату {self.room.get_room_number()} отменено.")

    def __str__(self):
        return (f"Бронирование комнаты {self.room.get_room_number()} с {self.check_in_date} по {self.check_out_date}. "
                f"Стоимость: {self.total_price} за {self.nights} ночей.")


class Hotel:
    """
    Класс для управления отелем
    """
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        if not isinstance(room, Room):
            raise TypeError("Добавляемый объект должен быть экземпляром класса Room или его подкласса.")
        self.rooms.append(room)

    def find_available_room(self):
        for room in self.rooms:
            if not room.is_booked():
                return room
        raise ValueError("Нет свободных номеров.")

    def __str__(self):
        return f"Отель {self.name} с {len(self.rooms)} номерами."