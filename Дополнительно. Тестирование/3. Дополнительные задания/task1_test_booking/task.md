Покрыть тестами классы:
* `Room`, `SingleRoom`, `DoubleRoom`, `Suite` используя `TestRoom`;
* `Booking`используя `TestBooking`;
* `Hotel` используя `TestHotel`;

Проверить процент покрытия тестами


### Возможная реализация для проверки (полный код)

<div class="hint">

```python
class TestRoom(unittest.TestCase):

    def test_room_initialization(self):
        room = Room(101, 100)
        self.assertEqual(room.get_room_number(), 101)
        self.assertEqual(room.calculate_price(1), 100)
        self.assertFalse(room.is_booked())

    def test_room_booking(self):
        room = Room(101, 100)
        room.book()
        self.assertTrue(room.is_booked())
        with self.assertRaises(ValueError):
            room.book()  # Попытка повторно забронировать комнату

    def test_room_unbooking(self):
        room = Room(101, 100)
        room.book()
        room.unbook()
        self.assertFalse(room.is_booked())
        with self.assertRaises(ValueError):
            room.unbook()  # Попытка снять бронь с не забронированной комнаты

    def test_suite_price_calculation(self):
        suite = Suite(201, 200)
        total_price = suite.calculate_price(3)
        expected_price = 200 * 3 * 1.2  # 20% надбавка
        self.assertEqual(total_price, expected_price)


class TestBooking(unittest.TestCase):

    def setUp(self):
        self.room = Room(101, 100)
        self.check_in = date(2023, 9, 1)
        self.check_out = date(2023, 9, 4)
        self.booking = Booking(self.room, self.check_in, self.check_out)

    def test_booking_initialization(self):
        self.assertEqual(self.booking.nights, 3)
        self.assertEqual(self.booking.total_price, 300)  # 100 * 3

    def test_confirm_booking(self):
        self.booking.confirm_booking()
        self.assertTrue(self.room.is_booked())

    def test_cancel_booking(self):
        self.booking.confirm_booking()
        self.booking.cancel_booking()
        self.assertFalse(self.room.is_booked())

    def test_booking_with_invalid_room(self):
        with self.assertRaises(TypeError):
            Booking("not_a_room", self.check_in, self.check_out)


class TestHotel(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel("Grand Hotel")

    def test_add_room(self):
        room = Room(101, 100)
        self.hotel.add_room(room)
        self.assertEqual(len(self.hotel.rooms), 1)

    def test_find_available_room(self):
        room1 = Room(101, 100)
        room2 = Room(102, 150)
        self.hotel.add_room(room1)
        self.hotel.add_room(room2)
        self.assertEqual(self.hotel.find_available_room(), room1)
        room1.book()
        self.assertEqual(self.hotel.find_available_room(), room2)

    def test_find_no_available_room(self):
        room1 = Room(101, 100)
        room2 = Room(102, 150)
        room1.book()
        room2.book()
        self.hotel.add_room(room1)
        self.hotel.add_room(room2)
        with self.assertRaises(ValueError):
            self.hotel.find_available_room()
```
</div>
