import unittest
from datetime import datetime
from main import *  # импортируем то, что будем тестировать


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.book = AudioBook('Книга', 'Автор', 3.30)

    def test_get_name(self):
        self.assertEqual(self.book.name, 'Книга')

    def test_get_author(self):
        self.assertEqual(self.book.author, 'Автор')

    def test_set_name(self):
        self.book.name = 'Новая книга'
        self.assertEqual(self.book.name, 'Новая книга')

    def test_set_name_error(self):
        with self.assertRaises(TypeError):
            self.book.name = 123

    def test_validate_duration_error(self):
        with self.assertRaises(TypeError):
            self.book.validate_duration('123')

    def test_check_time(self):
        self.assertEqual(self.book.check_time(), datetime.now())

    @unittest.skip('Функция ничего не возвращает')
    def test_check_book_type(self):
        pass


if __name__ == '__main__':
    unittest.main()
