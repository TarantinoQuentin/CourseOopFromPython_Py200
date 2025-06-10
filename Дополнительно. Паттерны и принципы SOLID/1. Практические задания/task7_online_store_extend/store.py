from abc import abstractmethod


class ProductManagement:
    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def update_product(self, product):
        pass

    @abstractmethod
    def get_product(self, product_id):
        pass


class OrderManagement:
    @abstractmethod
    def place_order(self, order):
        pass

    @abstractmethod
    def get_order(self, order_id):
        pass


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price})"


class Order:
    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __str__(self):
        return f"Order(id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})"


class ProductRepository:
    def __init__(self):
        self.products = {}  # Используем словарь для хранения продуктов по их ID

    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Продукт с таким ID уже существует.")
        self.products[product.product_id] = product

    def update_product(self, product):
        if product.product_id not in self.products:
            raise ValueError("Продукт с таким ID не найден.")
        self.products[product.product_id] = product

    def get_product(self, product_id):
        if product_id not in self.products:
            raise ValueError(f"Продукт с ID {product_id} не найден.")
        return self.products[product_id]


class OrderRepository:
    def __init__(self):
        self.orders = {}  # Используем словарь для хранения заказов по их ID

    def place_order(self, order):
        if order.order_id in self.orders:
            raise ValueError("Заказ с таким ID уже существует.")
        self.orders[order.order_id] = order

    def get_order(self, order_id):
        if order_id not in self.orders:
            raise ValueError(f"Заказ с ID {order_id} не найден.")
        return self.orders[order_id]


# Реализация принципа инверсии зависимостей путем введения классов репозитория в качестве зависимостей
class OnlineStore(ProductManagement, OrderManagement):
    def __init__(self, product_repository, order_repository):
        self.product_repository = product_repository
        self.order_repository = order_repository

    def add_product(self, product):
        self.product_repository.add_product(product)

    def update_product(self, product):
        self.product_repository.update_product(product)

    def get_product(self, product_id):
        return self.product_repository.get_product(product_id)

    def place_order(self, order):
        self.order_repository.place_order(order)

    def get_order(self, order_id):
        return self.order_repository.get_order(order_id)