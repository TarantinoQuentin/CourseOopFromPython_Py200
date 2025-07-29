import hashlib
import random


class IdCounter:
    def __init__(self):
        self._current_id = 0

    def _increment_id(self):
        self._current_id += 1

    @property
    def current_id(self):
        return self._current_id

    def get_new_id(self):
        self._increment_id()
        return self.current_id


class Password:

    @classmethod
    def get(cls, password: str):
        if cls.is_valid(password):
            return hashlib.sha256(password.encode()).hexdigest()
        raise TypeError('Пароль должен быть строкой')

    @classmethod
    def check(cls, password: str, hash_password: str):
        if isinstance(hash_password, str):
            return cls.get(password) == hash_password
        raise TypeError('Хэш пароля должен быть строкой')

    @staticmethod
    def is_valid(password: str):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкового типа")
        if len(password) < 8:
            raise ValueError("Пароль должен быть длиной не менее 8 символов")
        if password.isalpha() or password.isdigit():
            raise ValueError("Пароль не соответствует минимальным требованиям")
        return True


class Product:
    _counter = IdCounter()

    def __init__(self, name: str, price: float, rating: float):

        self._id = self._counter.get_new_id()
        self._name = None
        self._set_name(name)
        self.price = price
        self.rating = rating

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def _set_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Значение должно быть типа str")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            if isinstance(value, int):
                value = float(value)
            else:
                raise TypeError("Значение должно быть вещественное")
        if value < 0:
            raise ValueError("Цена не должна быть отрицательной")
        self._price = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, float):
            if isinstance(value, int):
                value = float(value)
            else:
                raise TypeError("Значение должно быть вещественное")
        if value < 0:
            raise ValueError("Рейтинг не должен быть отрицательным")
        elif value > 5:
            print(value)
            raise ValueError("Рейтинг не должен быть > 5")
        self._rating = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, price={self.price}, rating={self.rating})"

    def __str__(self):
        return f"{self.id}_{self.name}"


class Cart:

    def __init__(self):
        self._data = []

    def add(self, product):
        self._data.append(product)

    def remove(self, product):
        self._data.remove(product)

    def get_data(self):
        return self._data


class User:
    _counter = IdCounter()

    def __init__(self, username: str, password: str):

        self._id = self._counter.get_new_id()
        self._username = None
        self._set_username(username)
        self.__password = Password.get(password)
        self._cart = Cart()

    @property
    def cart(self):
        return self._cart

    @property
    def username(self):
        return self._username

    def _set_username(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Значение должно быть типа str")
        self._username = value

    def __repr__(self):
        return f"{self.__class__.__name__}(username={self.username}, password='password1')"

    def __str__(self):
        return f"{self._id}_{self.username}"


class ProductGenerator:
    data = ["Яблоко", "Aпельсин", "Картошка", "Киви", "Огурец"]

    def get_name(self):
        return random.choice(self.data)

    def get_rating(self):
        return round(random.uniform(0, 5), 2)

    def get_price(self):
        return round(random.uniform(0, 200), 2)

    def get_product(self):
        return Product(self.get_name(), self.get_price(), self.get_rating())


class Store:
    def __init__(self, product_generator: ProductGenerator):
        self.user = None
        self.authentification()
        # self.categories = CategoryRepository()
        self.product_generator = product_generator

    def authentification(self):
        while True:
            login = input("Введите логин\n")
            password = input("Введите пароль\n")
            try:
                self.user = User(login, password)
                break
            except Exception as e:
                print(e)

    def add_to_cart(self):
        product = self.product_generator.get_product()
        print(product)
        self.user.cart.add(product)

    def view_cart(self):
        print(self.user.cart.get_data())


if __name__ == "__main__":
    s = Store(ProductGenerator())
    s.add_to_cart()
    s.add_to_cart()
    s.add_to_cart()
    s.add_to_cart()
    s.view_cart()
