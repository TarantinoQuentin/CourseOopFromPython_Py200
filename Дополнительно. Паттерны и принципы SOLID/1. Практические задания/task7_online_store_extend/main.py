from store import OnlineStore, ProductRepository, OrderRepository


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}"


class CustomerRepository:
    def __init__(self):
        # Используем словарь для хранения клиентов
        self.customers = {}

    def add_customer(self, customer):
        """Добавление клиента в репозиторий"""
        if customer.customer_id in self.customers:
            raise ValueError(f"Клиент с ID {customer.customer_id} уже существует.")
        self.customers[customer.customer_id] = customer
        print(f"Клиент {customer.name} добавлен.")

    def update_customer(self, customer):
        """Обновление информации о клиенте"""
        if customer.customer_id not in self.customers:
            raise ValueError(f"Клиент с ID {customer.customer_id} не найден.")
        self.customers[customer.customer_id] = customer
        print(f"Информация о клиенте {customer.customer_id} обновлена.")

    def get_customer(self, customer_id):
        """Извлечение клиента по ID"""
        if customer_id not in self.customers:
            raise ValueError(f"Клиент с ID {customer_id} не найден.")
        return self.customers[customer_id]

    def remove_customer(self, customer_id):
        """Удаление клиента из репозитория"""
        if customer_id not in self.customers:
            raise ValueError(f"Клиент с ID {customer_id} не найден.")
        del self.customers[customer_id]
        print(f"Клиент с ID {customer_id} удален.")


# Добавление функциональности управления клиентами в класс OnlineStore
class OnlineStoreWithCustomers(OnlineStore):
    def __init__(self, product_repository, order_repository, customer_repository):
        super().__init__(product_repository, order_repository)
        self.customer_repository = customer_repository

    def add_customer(self, customer):
        self.customer_repository.add_customer(customer)

    def update_customer(self, customer):
        self.customer_repository.update_customer(customer)

    def get_customer(self, customer_id):
        return self.customer_repository.get_customer(customer_id)


if __name__ == "__main__":
    # Создаем репозитории для продуктов, заказов и клиентов
    product_repo = ProductRepository()
    order_repo = OrderRepository()
    customer_repo = CustomerRepository()

    # Создаем экземпляр магазина с поддержкой управления клиентами
    store_with_customers = OnlineStoreWithCustomers(product_repo, order_repo, customer_repo)

    # Работа с клиентами
    customer = Customer(1, "John Doe")
    store_with_customers.add_customer(customer)

