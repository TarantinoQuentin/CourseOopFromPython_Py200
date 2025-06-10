import unittest

from task import Glass


class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.glass = Glass(200, 100)

    def test_add(self):
        self.glass.add_water(50)
        self.assertEqual(self.glass.occupied_volume, 150, msg="Некорректно работает метод add_water")

    def test_remove(self):
        self.glass.remove_water(50)
        self.assertEqual(self.glass.occupied_volume, 50, msg="Некорректно работает метод remove_water")

    def test_add_error(self):
        with self.assertRaises(TypeError,
                               msg='Метод add_water должен проходить проверку на тип. Только int или float'):
            self.glass.add_water('500')

        with self.assertRaises(ValueError,
                               msg='Метод add_water должен проходить проверку на то, что нельзя перелить больше объёма стакана.'):
            self.glass.add_water(500)

        with self.assertRaises(ValueError,
                               msg='Метод add_water должен проходить проверку на то, что нельзя добавить отрицательное значение.'):
            self.glass.add_water(-5)

    def test_remove_error(self):
        with self.assertRaises(TypeError,
                               msg='Метод remove_water должен проходить проверку на тип. Только int или float'):
            self.glass.remove_water('500')

        with self.assertRaises(ValueError,
                               msg='Метод remove_water должен проходить проверку на то, что нельзя вылить больше чем есть.'):
            self.glass.remove_water(500)

        with self.assertRaises(ValueError,
                               msg='Метод remove_water должен проходить проверку на то, что нельзя добавить отрицательное значение.'):
            self.glass.remove_water(-5)
