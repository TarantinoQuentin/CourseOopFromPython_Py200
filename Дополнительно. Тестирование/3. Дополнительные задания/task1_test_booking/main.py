import unittest
from datetime import date

# Все ваши классы определены в модуле room_booking, поэтому делаем import
from room_booking import Room, SingleRoom, DoubleRoom, Suite, Booking, Hotel


class TestRoom(unittest.TestCase):
    """
    Класс для тестирования работы классов Room, SingleRoom, DoubleRoom, Suite
    """


class TestBooking(unittest.TestCase):
    """
    Класс для тестирования работы класса Booking
    """


class TestHotel(unittest.TestCase):
    """
    Класс для тестирования работы класса Hotel
    """


if __name__ == "__main__":
    unittest.main()
