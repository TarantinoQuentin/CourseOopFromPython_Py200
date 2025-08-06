import re
import hashlib
import random


class IdCounter:
    """
    Класс — счетчик ID
    """

    def __init__(self):
        self._current_id = 0

    @property
    def current_id(self) -> int:
        """
        Метод возвращающий текущий ID
        :return: значение ID
        """
        return self._current_id

    def get_new_id(self) -> int:
        """
        Метод возвращающий следующий ID
        :return: значение ID
        """
        self._current_id += 1
        return self.current_id


class Password:
    """
    Класс для управления паролями
    """

    @classmethod
    def get_hash_password(cls, password: str) -> str:
        """
        Метод проверяет соответствие пароля требованиям и возвращает его хэш-значение
        :return: хэш-значение пароля пользователя
        """
        if cls.is_valid_password(password):
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            return password_hash
        raise ValueError('Значение пароля не соответствует требованиям')

    @classmethod
    def is_valid_password(cls, password: str) -> bool:
        """
        Метод для проверки пароля на соответствие требованиям
        :param password: пароль пользователя
        :raise: TypeError, если пароль не строкового типа
        :raise: ValueError, если пароль не соответствует требованиям
        :return: True, если пароль прошел проверку
        """
        if not isinstance(password, str):
            raise TypeError('Пароль должен быть типа str')
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            raise ValueError('Пароль не соответствует требованиям, он должен быть длиной не менее 8 символов и содержать как буквы латиницы, так и цифры')
        return True

    @classmethod
    def check_password(cls, password: str, hashpassword: str) -> bool:
        """
        Метод для сверки пароля с хэш-значением
        :param hashpassword: передаваемое хэш-значение пароля
        :param password: передаваемый пароль
        :raise: TypeError, если значение пароля не соответствует требованиям
        :return: булево значение
        """
        if isinstance(hashpassword, str):
            return cls.get_hash_password(password) == hashpassword
        raise TypeError('Хэш-значение пароля не строкового типа')


class Product:
    """
    Класс продукт
    """

    _id_counter = IdCounter()

    def __init__(self, name: str, price: int | float, rating: int | float):
        """
        Подготовка класса 'продукт' к работе
        :param name: название продукта
        :param price: цена
        :param rating: рейтинг
        """
        self._id_ = self._id_counter.get_new_id()
        self.validate_name(name)
        self._name = name
        self.price = price
        self.rating = rating

    @property
    def price(self) -> int|float:
        """
        Метод-свойство для получения неизменяемого значения названия цены продукта
        :return: цена товара
        """
        return self._price

    @price.setter
    def price(self, value: int | float) -> None:
        """
        Метод проверяет значение переданной цены и устанавливает ее атрибуту
        :param value: цена продукта
        :raise: возвращает TypeError, если значение цены не соответствует типу int или float
        :raise: возвращает ValueError, если значение отрицательно или равно нулю
        :return: None
        """
        if not isinstance(value, int | float):
            raise TypeError('Значение цены должно быть типа int или float')
        if value <= 0:
            raise ValueError('Значение цены должно быть положительным')
        self._price = value

    @property
    def rating(self) -> int|float:
        """
        Метод-свойство для получения неизменяемого значения названия рейтинга продукта
        :return: рейтинг товара
        """
        return self._rating

    @rating.setter
    def rating(self, value: int | float) -> None:
        """
        Метод проверяет значение переданного рейтинга и устанавливает его атрибуту
        :param value: рейтинг продукта
        :raise: возвращает TypeError, если значение рейтинга не соответствует типу int или float
        :raise: возвращает ValueError, если значение рейтинга отрицательное или больше 10-ти
        :return: None
        """
        if not isinstance(value, int | float):
            raise TypeError('Значение рейтинга должно быть типа int или float')
        if not 0 <= value <= 10:
            raise ValueError('Значение рейтинга должно быть не более 10-ти, положительным или равно нулю')
        self._rating = value

    @property
    def id_(self) -> int:
        """
        Метод-свойство для получения неизменяемого значения названия ID продукта
        :return: возвращает значение ID
        """
        return self._id_

    def validate_name(self, name: str) -> None:
        """
        Метод проверяет значение переданного названия
        :param name: название продукта
        :raise: возвращает TypeError, если название не строкового типа
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('Название должно быть типа str')

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
        return f'{self.__class__.__name__}(name={self.name!r}, price={self.price}, rating={self.rating})'


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
            return 'Корзина пуста'
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


class User:
    """
    Класс 'Пользователь'
    """

    _id_counter = IdCounter()

    def __init__(self, username: str, password: str):
        """
        Подготовка класса 'пользователь' к работе
        :param username: логин пользователя
        :param password: пароль пользователя
        """
        self._id_ = self._id_counter.get_new_id()
        self.validate_username(username)
        self._username = username
        self._password = Password().get_hash_password(password)
        self._cart = Cart()

    @property
    def cart(self) -> Cart:
        """
        Метод возвращает защищенный атрибут — корзину
        :return: корзина пользователя
        """
        return self._cart

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
        if not re.match(r'^[A-za-z\d_]+$', username):
            raise ValueError('Имя пользователя может содержать только латиницу, цифры и нижнее подчеркивание')

    def __str__(self):
        return f'{self._id_}_{self.username}'

    def __repr__(self):
        return f"{self.__class__.__name__}(username={self.username}, password='password1')"

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

class Store:
    """
    Класс 'магазин'
    """


    def __init__(self, product_generator: ProductGenerator):
        """
        Подготовка к работе класса 'магазин'
        :param product_generator: класс-генератор продуктов
        """
        self.user = None
        self.product_generator = product_generator
        self.authentification()

    def authentification(self):
        while True:
            username = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            try:
                self.user = User(username, password)
                break
            except Exception as error:
                print(error)

    def get_random_product_in_cart(self) -> None:
        """
        Метод для добавления случайного продукта в корзину пользователя
        :return: None
        """
        return self.user.cart.add_to_cart(self.product_generator.generate_product())

    def view_cart(self):
        """
        Метод для просмотра корзины пользователя
        :return: возвращает список продуктов в корзине пользователя или сообщение о том, что корзина пуста
        """
        return self.user.cart.get_user_cart()


class Category:
    """
    Класс 'категория' товара
    """

    def __init__(self, name: str):
        """
        Подготовка к работе класса 'категория'
        :param name: название категории
        """
        self.product_list = []
        self.validate_name(name)
        self._name = name

    @property
    def name(self) -> str:
        """
        Метод-свойство для возврата названия категории, защищенного от изменения
        :return: название категории
        """
        return self._name

    def get_category_list(self) -> list[Product | None] | str:
        """
        Метод для получения списка товаров в категории
        :return: возвращает список продуктов в категории или сообщение о том, что категория пуста
        """
        if not self.product_list:
            return 'Категория пуста'
        return self.product_list

    def validate_name(self, name: str) -> None:
        """
        Метод для валидации названия категории
        :param name: название категории
        :raise: TypeError, если название не строкового типа
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError('Название категории должно быть строковым типом')

    def remove_from_category(self, product: Product) -> None:
        """
        Метод для удаления товара из категории
        :param product: удаляемый продукт
        :raise: возвращает ValueError, если товар не найден в категории
        :return: None
        """
        if product not in self.product_list:
            raise ValueError('Товар не найден в корзине')
        self.product_list.remove(product)

    def add_to_category(self, product: Product) -> None:
        """
        Метод для добавления товара в категорию
        :param product: добавляемый продукт
        :raise: ValueError, если добавляемый продукт уже есть в категории
        :return: None
        """
        if product in self.product_list:
            raise ValueError('Такой продукт уже есть в категории')
        self.product_list.append(product)

    def __str__(self):
        return self._name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name})'


class CategoryRepository:
    """
    Класс-хранилище категорий товаров
    """

    def __repr__(self):
        self.categories_list = []

    def add_category_to_repository(self, category: Category) -> None:
        """
        Метод для добавления категории в хранилище
        :param category: категория товаров
        :raise: ValueError, если такая категория уже есть в списке
        :return: None
        """
        if category not in self.categories_list:
            self.categories_list.append(category)
        else:
            raise ValueError('Такая категория уже есть в списке')


    def get_all_categories(self) -> list[Category | None]:
        """
        Метод возвращает список всех категорий товаров в хранилище
        :return: список категорий
        """
        return self.categories_list

    def get_specific_category(self, category_name: str):
        """
        Метод возвращает искомую категорию товаров
        :param category_name: название категории товаров
        :raise: ValueError, если категория товаров не найдена
        :return: искомая категория товаров
        """
        for category in self.categories_list:
            if category.name == category_name:
                return category
            raise ValueError('Искомая категория не найдена')


class CartExtended(Cart):
    """
    Улучшенный класс 'корзина'
    """

    def __init__(self):
        """
        Подготовка класса 'расширенная корзина' к работе
        """
        super().__init__()
        self._user_cart = {}

    def add_category_to_cart(self, category: Category) -> None:
        """
        Метод для добавления в корзину товаров категориями
        :param category: категория товаров
        :raise: ValueError, если категория пуста
        :return: None
        """
        if category.product_list:
            for product in category.product_list:
                self.add_to_cart(product)
        else:
            raise ValueError('Категория пуста')

    def add_to_cart(self, product: Product) -> None:
        """
        Метод для добавления товара в корзину
        :param product: добавляемый продукт
        :raise: ValueError, если добавляемый продукт уже есть в корзине
        :return: None
        """
        if product in self._user_cart:
            self._user_cart[product] += 1
        self._user_cart[product] = 1

    def remove_from_cart(self, product: Product) -> None:
        """
        Метод для удаления товара из корзины
        :param product: удаляемый продукт
        :raise: возвращает ValueError, если товар не найден в корзине
        :return: None
        """
        if product not in self._user_cart:
            raise ValueError('Товар не найден в корзине')
        self._user_cart.pop(product)

    def change_product_price(self, product: Product, new_value: int | float) -> None:
        """
        Метод для изменения цены продукта в корзине
        :param product: продукт
        :param new_value: новое значение цены
        :raise: ValueError, если товар не найден в корзине
        :return: None
        """
        if product in self._user_cart:
            product.price = new_value
        else:
            raise ValueError('Товар не найден')

    def change_product_rating(self, product: Product, new_value: int | float) -> None:
        """
        Метод для изменения рейтинга продукта в корзине
        :param product: продукт
        :param new_value: новое значение рейтинга
        :raise: ValueError, если товар не найден в корзине
        :return: None
        """
        if product in self._user_cart:
            product.rating = new_value
        else:
            raise ValueError('Товар не найден')


class StoreExtended(Store):
    """
    Улучшенный класс 'магазин'
    """

    def __init__(self, product_generator: ProductGenerator):
        """
        Подготовка к работе класса 'улучшенный магазин'
        """
        super().__init__(product_generator)

    def change_user(self) -> None:
        """
        Метод для смены аккаунта пользователя, выходит из прошлого аккаунта и
        запускает аутентификацию в следующий
        :raise: ValueError, если пользователь не аутентифицирован
        :return: None
        """
        if self.user:
            self.user = None
            self.authentification()
        else:
            raise ValueError('Пользователь не аутентифицирован')


if __name__ == "__main__":
    # Проверьте функциональность добавления продуктов в корзину и отображения корзины пользователя
    store = Store(ProductGenerator())
    print(store.view_cart())
    store.get_random_product_in_cart()
    print(store.view_cart())
    for _ in range(5):
        store.get_random_product_in_cart()
    print(store.view_cart())
