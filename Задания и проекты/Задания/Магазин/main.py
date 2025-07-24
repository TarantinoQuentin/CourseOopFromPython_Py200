import re
from itertools import count, product
import hashlib
import random


class IdCounter:
    """
    Класс — счетчик ID
    """

    count = 0

    @classmethod
    def get_id(cls) -> int:
        """
        Метод возвращающий следующий ID
        :return: значение ID
        """
        cls.count += 1
        return cls.count


class Password:
    """
    Класс для управления паролями
    """

    def get_hash_password(self, password: str) -> str:
        """
        Метод проверяет соответствие пароля требованиям и возвращает его хэш-значение
        :raise: возвращает TypeError, если пароль не строкового типа
        :raise: возвращает ValueError, если пароль не соответствует предъявленным требованиям
        :return: хэш-значение пароля пользователя
        """

        if not isinstance(password, str):
            raise TypeError('Пароль должен быть типа str')
        if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            # hash_dict['password'] = hash_dict
            return password_hash
        raise ValueError('Пароль не соответствует требованиям, он должен быть длиной не менее 8 символов и содержать как буквы латиницы, так и цифры')

    def check_password(self, password: str, login: str, user_database: dict) -> bool:
        """
        Метод для сверки пароля с базой пользователей
        :param password: передаваемый пароль
        :param login: передаваемый логин
        :param user_database: база логинов и паролей пользователей
        :raise: возвращает TypeError, если логин не строкового типа
        :raise: возвращает ValueError, если пользователь с таким логином не найден
        :return: булево значение
        """
        if not isinstance(login, str):
            raise TypeError('Логин пользователя должен быть типа str')
        if login not in user_database:
            raise ValueError('Такого пользователя не существует')
        if user_database[login] == self.get_hash_password(password):
            return True
        return False



class Product(IdCounter):
    """
    Класс продукт
    """

    def __init__(self, name: str, price: int | float, rating: int | float):
        """
        Подготовка класса 'продукт' к работе
        :param name: название продукта
        :param price: цена
        :param rating: рейтинг
        """
        IdCounter.__init__(self)
        self._id_ = self.id_
        self.validate_name(name)
        self._name = name
        self.validate_price(price)
        self._price = price
        self.validate_rating(rating)
        self._rating = rating

    @property
    def id_(self) -> int:
        """
        Метод для определения ID продукта
        :return: возвращает значение ID вызывая классовый метод IdCounter
        """
        return super().get_id()

    def validate_name(self, name: str) -> None:
        """
        Метод проверяет значение переданного названия
        :param name: название продукта
        :raise: возвращает TypeError, если название не строкового типа
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('Название должно быть типа str')

    def validate_price(self, price: int | float) -> None:
        """
        Метод проверяет значение переданной цены
        :param price: цена продукта
        :raise: возвращает TypeError, если значение цены не соответствует типу int или float
        :raise: возвращает ValueError, если значение отрицательно или равно нулю
        :return: None
        """
        if not isinstance(price, int | float):
            raise TypeError('Значение цены должно быть типа int или float')
        if price <= 0:
            raise ValueError('Значение цены должно быть положительным')

    def validate_rating(self, rating: int | float) -> None:
        """
        Метод проверяет значение переданного рейтинга
        :param rating: рейтинг продукта
        :raise: возвращает TypeError, если значение рейтинга не соответствует типу int или float
        :raise: возвращает ValueError, если значение рейтинга отрицательное
        :return: None
        """
        if not isinstance(rating, int | float):
            raise TypeError('Значение рейтинга должно быть типа int или float')
        if rating < 0:
            raise ValueError('Значение рейтинга должно быть положительным или равно нулю')

    @property
    def name(self) -> str:
        """
        Метод-свойство для получения неизменяемого значения названия продукта
        :return: Название продукта
        """
        return self._name

    def __str__(self):
        return f'{self._id_}_{self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, price={self._price}, rating={self._rating})'


class Cart:
    """
    Класс корзина продуктов
    """

    def __init__(self):
        """
        Подготовка класса 'корзина' к работе
        """
        self._user_cart = []

    def get_user_cart(self) -> list[Product | None] | str:
        """
        Метод для получения списка товаров в корзине пользователя
        :return: возвращает список продуктов в корзине пользователя или сообщение о том, что корзина пуста
        """
        if not self._user_cart:
            return 'Cart is empty'
        return self._user_cart

    def remove_from_cart(self, product: Product) -> None:
        """
        Метод для удаления товара из корзины
        :param product: удаляемый продукт
        :raise: возвращает ValueError, если товар не найден в корзине
        :return: None
        """
        if product not in self._user_cart:
            raise ValueError('Товар не найден в корзине')
        self._user_cart.remove(product)

    def add_to_cart(self, product: Product) -> None:
        """
        Метод для добавления товара в корзину
        :param product: добавляемый продукт
        :raise: ValueError, если добавляемый продукт уже есть в корзине
        :return: None
        """
        if product in self._user_cart:
            raise ValueError('Такой продукт уже есть в корзине')
        self._user_cart.append(product)


class User(Cart):
    """
    Класс 'Пользователь'
    """

    user_id_count = 0

    @classmethod
    def get_user_id(cls) -> int:
        """
        Метод возвращающий следующий ID
        :return: значение ID
        """
        cls.user_id_count += 1
        return cls.user_id_count

    def __init__(self, username: str, password: str):
        """
        Подготовка класса 'пользователь' к работе
        :param username: логин пользователя
        :param password: пароль пользователя
        """
        Cart.__init__(self)
        self._id_ = User.user_id_count
        self.validate_username(username)
        self._username = username
        self._password = Password().get_hash_password(password)
        self._cart = self.cart

    @property
    def cart(self) -> list[Product | None]:
        """
        Метод возвращает защищенный атрибут — корзину
        :return: корзина пользователя
        """
        return super().get_user_cart()

    @property
    def username(self) -> str:
        """
        Метод возвращает защищенный атрибут — имя пользователя (логин)
        :return: имя пользователя (логин)
        """
        return self._username

    def validate_username(self, username: str) -> None:
        """
        Метод проверяет на соответствие передаваемое значение атрибута 'имя пользователя'
        :param username: имя пользователя (логин)
        :raise: TypeError, если имя пользователя не соответствует типу str
        :raise: ValueError, если имя пользователя содержит кириллицу
        :return: None
        """
        if not isinstance(username, str):
            raise TypeError('Имя пользователя должно быть типом str')
        if not re.match(r'^[a-z\d_]+$', username):
            raise ValueError('Имя пользователя может содержать только латиницу, цифры и нижнее подчеркивание')

    def __str__(self):
        return f'{self._id_}_{self.username}'

    def __repr__(self):
        return f"User(username={self.username}, password='password1')"

# Создайте генератор продуктов, чтобы при вызове функции или метода возвращался
# случайный продукт вашего направления магазина

class ProductGenerator:
    """
    Класс-генератор продуктов для магазина
    """

    def __init__(self):
        """
        Подготовка класса-генератора продуктов к работе
        """
        self.product_source = {'product_name': ['break_pads', 'oil_filter', 'spark_plugs', 'oil', 'clutch', 'shock_absorbers'],
                  'price_range': (100, 10000), 'rating_range': (0, 10)}

    def generate_product(self):
        """
        Метод-генератор случайных продуктов для магазина
        :return: возвращает класс продукт с атрибутами со случайным значением
        """
        return Product(name=random.choice(self.product_source['product_name']),
                price=round(random.randint(*(self.product_source['price_range'])), 2),
                rating=round(random.randint(*(self.product_source['rating_range'])), 2))

class Store(User, ProductGenerator):
    """
    Класс 'магазин'
    """

    text_username = 'Введите имя пользователя: '
    text_password = 'Введите пароль: '
    def __init__(self):
        """
        Подготовка к работе класса 'магазин'
        """
        User.__init__(self=self, username=input(self.text_username), password=input(self.text_password))
        ProductGenerator.__init__(self)

    def get_random_product_in_cart(self) -> None:
        """
        Метод для добавления случайного продукта в корзину пользователя
        :return: None
        """
        return super().add_to_cart(super().generate_product())

    def view_cart(self):
        """
        Метод для просмотра корзины пользователя
        :return: возвращает список продуктов в корзине пользователя или сообщение о том, что корзина пуста
        """
        return super().get_user_cart()


if __name__ == "__main__":
    # Проверьте функциональность добавления продуктов в корзину и отображения корзины пользователя
    store = Store()
    print(store.view_cart())
    store.get_random_product_in_cart()
    print(store.view_cart())
    store.get_random_product_in_cart()
    store.get_random_product_in_cart()
    store.get_random_product_in_cart()
    store.get_random_product_in_cart()
    store.get_random_product_in_cart()
    store.get_random_product_in_cart()
    print(store.view_cart())
