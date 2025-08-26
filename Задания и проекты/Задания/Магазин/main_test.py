import unittest
from main import Product, CartExtended, Category, User, Cart


class TestProduct(unittest.TestCase):
    """
    Класс для тестирования класса 'продукт'
    """

    def setUp(self) -> None:
        """
        Метод для создания экземпляра тестируемого класса
        :return: None
        """
        self.product = Product('belt', 1000, 10)

    def tearDown(self):
        """
        Метод для обнуления счетчика ID
        :return: None
        """
        Product._id_counter._current_id = 0

    def test_name(self) -> None:
        """
        Метод для тестирования геттера атрибута 'имя'
        :return: None
        """
        self.assertEqual(self.product.name, 'belt')

    def test_name_error(self) -> None:
        """
        Метод для вызова ошибки типа в методе, проверяющем тип значения имени продукта
        :return: None
        """
        with self.assertRaises(TypeError):
            self.product.validate_name(1000)

    def test_price(self) -> None:
        """
        Метод для тестирования геттера атрибута 'цена'
        :return: None
        """
        self.assertEqual(self.product.price, 1000)

    def test_price_type_error(self) -> None:
        """
        Метод для вызова ошибки типа в методе, устанавливающем цену на продукт, когда значение цены не соответствует корректному типу
        :return: None
        """
        with self.assertRaises(TypeError):
            self.product.price = '1000'

    def test_price_value_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, устанавливающем цену на продукт, когда значение некорректно
        :return: None
        """
        with self.assertRaises(ValueError):
            self.product.price = -1000

    def test_rating(self) -> None:
        """
        Метод для тестирования геттера атрибута 'рейтинг'
        :return: None
        """
        self.assertEqual(self.product.rating, 10)

    def test_rating_type_error(self) -> None:
        """
        Метод для вызова ошибки типа в методе, устанавливающем рейтинг продукта, когда значение рейтинга не соответствует корректному типу
        :return: None
        """
        with self.assertRaises(TypeError):
            self.product.rating = '10'

    def test_rating_value_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, устанавливающем рейтинг продукта, когда значение некорректно
        :return: None
        """
        with self.assertRaises(ValueError):
            self.product.rating = 20

    def test_id_(self) -> None:
        """
        Метод для тестирования геттера атрибута 'ID'
        :return: None
        """
        self.assertEqual(self.product.id_, 1)

class TestCartExtended(unittest.TestCase):
    """
    Класс для тестирования класса 'расширенная корзина'
    """

    def setUp(self) -> None:
        """
        Метод для создания экземпляра тестируемого класса
        :return: None
        """
        self.cart = CartExtended()
        self.category = Category('oils')
        self.product_one = Product('engine_oil', 1000, 10)
        self.product_two = Product('gearbox_oil', 2000, 9)
        self.category.add_to_category(self.product_two)
        self.cart.add_to_cart(self.product_one)

    def tearDown(self):
        """
        Метод для обнуления счетчика ID
        :return: None
        """
        Product._id_counter._current_id = 0

    def test_get_user_cart(self) -> None:
        """
        Метод для тестирования метода, возвращающего корзину пользователя или сообщение о том, что она пуста
        :return: None
        """
        self.assertEqual(self.cart.get_user_cart(), {self.product_one: 1})

    def test_add_to_cart(self) -> None:
        """
        Метод для тестирования метода добавления товара в корзину
        :return: None
        """
        self.cart.add_to_cart(self.product_two)
        self.assertTrue(self.product_two in self.cart.get_user_cart())

    def test_remove_from_cart(self) -> None:
        """
        Метод для тестирования метода удаления товара из корзины
        :return: None
        """
        self.cart.add_to_cart(self.product_two)  # добавляем второй товар в корзину, чтоб она не оказалась пустой после удаления первого, иначе будет сообщение
        self.cart.remove_from_cart(self.product_one)
        self.assertTrue(self.product_one not in self.cart.get_user_cart())

    def test_remove_from_cart_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, удаляющем продукт из корзины, когда товар отсутствует в корзине
        :return: None
        """
        with self.assertRaises(ValueError):
            self.cart.remove_from_cart(self.product_two)

    def test_add_category_to_cart(self) -> None:
        """
        Метод для тестирования метода, добавляющего товары, содержащиеся в конкретной категории
        :return: None
        """
        self.cart.add_category_to_cart(self.category)
        self.assertTrue(self.product_two in self.cart.get_user_cart())

    def test_add_category_to_cart_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, добавляющем категорию продуктов в корзину, когда категория не содержит товаров
        :return: None
        """
        with self.assertRaises(ValueError):
            self.cart.add_category_to_cart(Category('bulbs'))

    def test_change_product_price(self) -> None:
        """
        Метод для тестирования метода, изменяющего цену продукта, содержащегося в корзине
        :return: None
        """
        self.cart.change_product_price(self.product_one, 800)
        self.assertEqual(self.product_one.price, 800)

    def test_change_product_price_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, изменяющем цену продукта в корзине, когда товар отсутствует в корзине
        :return: None
        """
        with self.assertRaises(ValueError):
            self.cart.change_product_price(self.product_two, 1000)

    def test_change_product_rating(self) -> None:
        """
        Метод для тестирования метода, изменяющего рейтинг продукта, содержащегося в корзине
        :return: None
        """
        self.cart.change_product_rating(self.product_one, 5)
        self.assertEqual(self.product_one.rating, 5)

    def test_change_product_rating_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, изменяющем рейтинг продукта в корзине, когда товар отсутствует в корзине
        :return: None
        """
        with self.assertRaises(ValueError):
            self.cart.change_product_rating(self.product_two, 10)


class TestCategory(unittest.TestCase):
    """
    Класс для тестирования класса 'категория'
    """

    def setUp(self) -> None:
        """
        Метод для создания экземпляра тестируемого класса
        :return: None
        """
        self.category = Category('filters')
        self.product = Product('air_filter', 500, 7)

    def tearDown(self):
        """
        Метод для обнуления счетчика ID
        :return: None
        """
        Product._id_counter._current_id = 0

    def test_name(self) -> None:
        """
        Метод для тестирования метода, возвращающего имя категории
        :return: None
        """
        self.assertEqual(self.category.name, 'filters')

    def test_name_error(self) -> None:
        """
        Метод для вызова ошибки типа в методе, проверяющем значение имени категории, когда значение имени имеет некорректный тип
        :return: None
        """
        with self.assertRaises(TypeError):
            self.category.validate_name(1000)

    def test_get_category_list(self) -> None:
        """
        Метод для тестирования метода, возвращающего список продуктов в категории или сообщение о том, что она пуста
        :return: None
        """
        self.category.add_to_category(self.product)
        self.assertEqual(*self.category.get_category_list(), self.product)

    def test_remove_from_category(self) -> None:
        """
        Метод для тестирования метода, удаляющего товар из категории
        :return: None
        """
        self.category.add_to_category(self.product)  # добавляем товар, чтобы удалить далее
        self.category.remove_from_category(self.product)
        self.assertEqual(self.category.get_category_list(), 'Категория пуста')  # проверяем, что категория не содержит товаров

    def test_remove_from_category_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, удаляющем товар из категории, если товар не содержится в категории
        :return: None
        """
        with self.assertRaises(ValueError):
            self.category.remove_from_category(self.product)

    def test_add_to_category(self) -> None:
        """
        Метод для тестирования метода, добавляющего товар в категорию
        :return: None
        """
        self.category.add_to_category(self.product)
        self.assertEqual(*self.category.get_category_list(), self.product)

    def test_add_to_category_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, добавляющем товар в категорию, если товар уже есть в категории
        :return: None
        """
        self.category.add_to_category(self.product)
        with self.assertRaises(ValueError):
            self.category.add_to_category(self.product)


class TestUser(unittest.TestCase):
    """
    Класс для тестирования класса 'пользователь'
    """

    def setUp(self) -> None:
        """
        Метод для создания экземпляра тестируемого класса
        :return: None
        """
        self.user = User('username', 'pass1234')
        self.user_cart = Cart()

    def tearDown(self):
        """
        Метод для обнуления счетчика ID
        :return: None
        """
        Product._id_counter._current_id = 0

    def test_cart(self) -> None:
        """
        Метод для тестирования метода, возвращающего объект корзины пользователя
        :return: None
        """
        self.assertTrue(type(self.user.cart), type(self.user_cart))

    def test_username(self) -> None:
        """
        Метод для тестирования метода, возвращающего имя пользователя
        :return: None
        """
        self.assertEqual(self.user.username, 'username')

    def test_validate_username_type_error(self) -> None:
        """
        Метод для вызова ошибки типа в методе, проверяющем значение имени пользователя,
        если имя пользователя имеет некорректный тип данных
        :return: None
        """
        with self.assertRaises(TypeError):
            self.user.validate_username(12345)

    def test_validate_username_value_error(self) -> None:
        """
        Метод для вызова ошибки значения в методе, проверяющем значение имени пользователя,
        если имя пользователя не соответствует требованиям
        :return: None
        """
        with self.assertRaises(ValueError):
            self.user.validate_username('Имя пользователя')


if __name__ == "__main__":
    unittest.main()
