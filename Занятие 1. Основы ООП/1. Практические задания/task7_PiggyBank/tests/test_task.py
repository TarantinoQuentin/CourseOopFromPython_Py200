import unittest

from task import PiggyBank, Coin


# todo: replace this with an actual test
class TestPiggyBank(unittest.TestCase):
    def setUp(self):
        """
        Инициализация объектов для тестов.
        """
        self.piggy_bank = PiggyBank()
        self.coin1 = Coin(1.0)
        self.coin2 = Coin(0.5)
        self.coin3 = Coin(0.25)

    def test_add_coin(self):
        """
        Тест добавления монет в копилку.
        """
        self.piggy_bank.add_coin(self.coin1)
        self.piggy_bank.add_coin(self.coin2)
        self.assertEqual(len(self.piggy_bank.coins), 2)
        self.assertIn(self.coin1, self.piggy_bank.coins)
        self.assertIn(self.coin2, self.piggy_bank.coins)

    def test_break_piggy_bank(self):
        """
        Тест разбивания копилки и проверки содержимого.
        """
        self.piggy_bank.add_coin(self.coin1)
        self.piggy_bank.add_coin(self.coin2)
        self.piggy_bank.add_coin(self.coin3)

        expected_total_amount = self.coin1.denomination + self.coin2.denomination + self.coin3.denomination
        expected_coin_count = {1.0: 1, 0.5: 1, 0.25: 1}

        coin_count = self.piggy_bank.break_piggy_bank()
        self.assertEqual(sum(denom * count for denom, count in coin_count.items()), expected_total_amount)
        self.assertEqual(coin_count, expected_coin_count)
        self.assertEqual(len(self.piggy_bank.coins), 0)

    def test_add_coin_after_break(self):
        """
        Тест добавления монеты в разбитую копилку.
        """
        self.piggy_bank.add_coin(self.coin1)
        self.piggy_bank.break_piggy_bank()
        with self.assertRaises(ValueError):
            self.piggy_bank.add_coin(self.coin2)

    def test_break_piggy_bank_twice(self):
        """
        Тест повторного разбивания копилки.
        """
        self.piggy_bank.add_coin(self.coin1)
        self.piggy_bank.break_piggy_bank()
        with self.assertRaises(ValueError):
            self.piggy_bank.break_piggy_bank()
