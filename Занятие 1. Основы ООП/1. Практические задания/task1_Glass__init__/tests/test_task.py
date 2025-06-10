import unittest

from task import Glass


class TestGlass(unittest.TestCase):

    def test_valid_glass(self):
        glass = Glass(500, 300)
        self.assertEqual(glass.capacity_volume, 500)
        self.assertEqual(glass.occupied_volume, 300)

    def test_capacity_volume_type_error(self):
        with self.assertRaises(TypeError, msg='Параметр capacity_volume должен проходить проверку на тип. Только int или float'):
            Glass("500", 300)

    def test_capacity_volume_value_error(self):
        with self.assertRaises(ValueError, msg='Объем стакана должен быть больше 0'):
            Glass(0, 300)
        with self.assertRaises(ValueError, msg='Объем стакана должен быть больше 0'):
            Glass(-500, 300)

    def test_occupied_volume_type_error(self):
        with self.assertRaises(TypeError, msg='Параметр occupied_volume должен проходить проверку на тип. Только int или float'):
            Glass(500, "300")

    def test_occupied_volume_value_error(self):
        with self.assertRaises(ValueError, msg='Заполненность стакан не может быть отрицательной'):
            Glass(500, -300)

    def test_occupied_volume_greater_than_capacity(self):
        with self.assertRaises(ValueError, msg='Стакан не может быть заполнен больше чем на свой объём'):
            Glass(500, 600)
