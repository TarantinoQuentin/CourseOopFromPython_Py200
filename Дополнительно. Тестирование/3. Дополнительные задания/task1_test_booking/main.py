import unittest
from datetime import date

# Все ваши классы определены в модуле room_booking, поэтому делаем import
from room_booking import Room, SingleRoom, DoubleRoom, Suite, Booking, Hotel


class TestRoom(unittest.TestCase):
    """
    Класс для тестирования работы классов Room, SingleRoom, DoubleRoom, Suite
    """

    def test_room_init(self):
        self.room = Room(1, 300)
        self.assertEqual(self.room.get_room_number(), 1)
        self.assertEqual(self.room.calculate_price(1), 300)
        self.assertFalse(self.room.is_booked())

    def test_book(self):
        self.room = Room(1, 300)
        self.room.book()
        self.assertTrue(self.room.is_booked())
        with self.assertRaises(ValueError):
            self.room.book()

    def test_unbook(self):
        self.room = Room(1, 300)
        self.room.book()
        self.room.unbook()
        self.assertFalse(self.room.is_booked())
        with self.assertRaises(ValueError):
            self.room.unbook()

    def test_suite(self):
        self.suite = Suite(1, 300)
        self.assertEqual(self.suite.calculate_price(1), 360)


class TestBooking(unittest.TestCase):
    """
    Класс для тестирования работы класса Booking
    """

    def setUp(self):
        self.room = Room(1, 300)
        self.check_in = date(2025, 7, 7)
        self.check_out = date(2025, 8, 8)
        self.booking = Booking(self.room, self.check_in, self.check_out)

    def test_booking_error(self):
        with self.assertRaises(TypeError):
            Booking('1', self.check_in, self.check_out)

    def test_confirm_booking(self):
        self.booking.confirm_booking()
        self.assertTrue(self.room.is_booked())

    def test_cancel_booking(self):
        self.test_confirm_booking()
        self.booking.cancel_booking()
        self.assertFalse(self.room.is_booked())


class TestHotel(unittest.TestCase):
    """
    Класс для тестирования работы класса Hotel
    """

    def setUp(self):
        self.hotel = Hotel('Grand Hotel')
        self.room = Room(1, 500)
        self.room.book()
        self.hotel.add_room(self.room)

    def test_add_room_error(self):
        with self.assertRaises(TypeError):
            self.hotel.add_room('room')

    def test_find_room_error(self):
        with self.assertRaises(ValueError):
            self.hotel.find_available_room()

    def test_add_room(self):
        room_two = Room(2, 100)
        self.hotel.add_room(room_two)
        self.assertEqual(len(self.hotel.rooms), 2)

    def test_find_room(self):
        room_two = Room(2, 100)
        self.hotel.add_room(room_two)
        self.assertEqual(self.hotel.find_available_room(), room_two)


if __name__ == "__main__":
    unittest.main()
