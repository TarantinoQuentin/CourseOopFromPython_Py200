import unittest
from main import Item, Inventory, ItemManagement, MerchantsShop


class TestItem(unittest.TestCase):
    """
    Класс для тестирования работы класса 'вещь'
    """

    def test_item_init(self):
        self.item = Item('Sword', 1000)
        self.assertEqual(self.item._name, 'Sword')
        self.assertEqual(self.item._price, 1000)


class TestInventory(unittest.TestCase):
    """
    Класс для тестирования работы класса 'инвентарь'
    """

    def setUp(self):
        self.our_item = Item('Sword', 1000)
        self.current_inventory = Inventory()

    def test_add_item(self):
        # our_item = Item('Sword', 1000)
        # self.current_inventory = Inventory()
        self.current_inventory.add_item(self.our_item)
        self.assertTrue(self.our_item in self.current_inventory._inventory)

    def test_sold_item(self):
        self.current_inventory.add_item(self.our_item)
        self.current_inventory.sold_item(self.our_item)
        self.assertTrue(self.our_item not in self.current_inventory._inventory)

    def test_sold_item_error(self):
        with self.assertRaises(ValueError):
            self.current_inventory.sold_item(self.our_item)
        self.current_inventory.add_item(self.our_item)
        with self.assertRaises(ValueError):
            self.current_inventory.sold_item(self.our_item,2)


class TestMerchantsShop(unittest.TestCase):
    """
    Класс для тестирования работы класса 'магазин торговца'
    """

    def setUp(self):
        self.our_item = Item('Sword', 1000)
        self.current_inventory = Inventory()
        self.merchantsshop = MerchantsShop(self.current_inventory)

    def test_add_item(self):
        self.merchantsshop.add_item(self.our_item, 1)
        self.assertTrue(self.our_item in self.current_inventory._inventory)
        self.merchantsshop.sold_item(self.our_item, 1)
        self.assertFalse(self.our_item in self.current_inventory._inventory)



if __name__ == "__main__":
    unittest.main()