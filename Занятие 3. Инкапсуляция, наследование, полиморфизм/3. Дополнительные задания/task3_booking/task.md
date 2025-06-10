# Система бронирования отелей

### Описание: 
Приложение для управления бронированиями номеров в отелях.

Для реализации системы бронирования отелей, допишите несколько классов, 
которые будут моделировать комнаты в отеле, бронирование, и сам отель.

### Структура классов:
* Класс `Room` — базовый класс для всех типов комнат.
* Подклассы `SingleRoom`, `DoubleRoom`, `Suite` — конкретные типы комнат, наследующие от Room.
* Класс `Booking` — класс для управления бронированиями.
* Класс `Hotel` — класс для управления отелем и его номерами.


### Описание реализации:

1. Класс `Room` (базовый класс для номеров):
* Атрибуты:
  * `__room_number`: номер комнаты.
  * `__price_per_night`: цена за ночь.
  * `__is_booked`: флаг, указывающий, забронирована ли комната.

* Методы:
  * `__init__(self, room_number, price_per_night)`: конструктор, который инициализирует номер комнаты, цену за ночь и устанавливает статус комнаты как "не забронирована".
  * `book(self)`: метод, который бронирует комнату, если она не была забронирована, иначе выбрасывает ошибку.
  * `unbook(self)`: снимает бронь с комнаты, если она была забронирована.
  * `calculate_price(self, nights)`: вычисляет стоимость проживания, умножая цену за ночь на количество ночей.
  * `get_room_number(self)`: возвращает номер комнаты.
  * `is_booked(self)`: проверяет, забронирована ли комната.
  * `__str__(self)`: возвращает строковое представление объекта, указывая статус ("Забронирована" или "Свободна") и цену за ночь.

2. Классы `SingleRoom`, `DoubleRoom` и `Suite` (подклассы Room):
Эти классы представляют разные типы номеров:

> `SingleRoom` и `DoubleRoom` просто наследуют от `Room` без изменений.

> `Suite` переопределяет метод `calculate_price`, добавляя 20% наценку (люксовый налог).

3. Класс `Booking` (для управления бронированием):
Этот класс отвечает за бронирование конкретной комнаты:

* Атрибуты:
  * `room`: объект класса Room (или его подклассов).
  * `check_in_date`, check_out_date: даты заезда и выезда.
  * `nights`: количество ночей (вычисляется на основе разницы между датами заезда и выезда).
  * `total_price`: общая стоимость бронирования (вычисляется методом calculate_price объекта room).

* Методы:
  * `confirm_booking(self)`: бронирует комнату и выводит информацию о подтверждении бронирования.
  * `cancel_booking(self)`: снимает бронь с комнаты.
  * `__str__(self)`: возвращает строковое описание бронирования.

4. Класс `Hotel` (для управления отелем):
Этот класс управляет номерами в отеле:

* Атрибуты:
  * `name`: имя отеля.
  * `rooms`: список номеров в отеле (экземпляров класса Room или его подклассов).

* Методы:
  * `add_room(self, room)`: добавляет комнату в список номеров отеля.
  * `find_available_room(self)`: находит первый доступный номер (не забронированный). Если все номера забронированы, выбрасывает ошибку.
  * `__str__(self)`: возвращает строковое представление отеля с указанием количества номеров.


### Возможная реализация для проверки (полный код)

<div class="hint">

```python
from datetime import date


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
```

</div>
