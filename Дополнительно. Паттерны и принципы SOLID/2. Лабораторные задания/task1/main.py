from abc import abstractmethod


class Item:
    """
    Класс для вещи в игровом инвентаре
    """

    def __init__(self, name: str, price: int) -> None:
        """
        Подготовка для работы класса 'вещь'
        :param name: название вещи
        :param price: цена
        """
        self._name = name
        self._price = price
    
    def __str__(self):
        return f'Item(name={self._name}, price={self._price})'


class Inventory:
    """
    Класс для игрового инвентаря
    """

    def __init__(self):
        """
        Подготовка для работы класса 'инвентарь'
        """
        self._inventory = {}
    
    def add_item(self, item: Item, amount: int = 1) -> None:
        """
        Метод для добавления вещи в инвентарь
        :param item: вещь
        :param amount: количество
        :return: None
        """
        if item in self._inventory:
            self._inventory[item] += amount
        else:
            self._inventory[item] = amount

    def sold_item(self, item: Item, amount: int = 1) -> None:
        """
        Метод для продажи вещей из инвентаря
        :param item: вещь
        :param amount: количество
        :return: None
        """
        if item not in self._inventory:
            raise ValueError('Такой вещи нет в инвентаре.')

        if self._inventory[item] < amount:
            raise ValueError(f'Недостаточное количество, доступно {self._inventory[item]}')
        elif self._inventory[item] == amount:
            self._inventory.pop(item)
        else:
            self._inventory[item] -= amount


class ItemManagement:
    @abstractmethod
    def add_item(self, item, amount):
        pass

    @abstractmethod
    def sold_item(self, item, amount):
        pass


class MerchantsShop(ItemManagement):
    """
    Класс для лавки торговца
    """

    def __init__(self, player_inventory: Inventory):
        """
        Подготовка к работе класса 'лавка торговца'
        :param player_inventory: инвентарь игрока
        """
        self.player_inventory = player_inventory

    def add_item(self, item: Item, amount: int) -> None:
        """
        Метод для добавления вещи в инвентарь
        :param item: вещь
        :param amount: количество
        :return: None
        """
        self.player_inventory.add_item(item, amount)

    def sold_item(self, item: Item, amount: int) -> None:
        """
        Метод для продажи вещей из инвентаря
        :param item: вещь
        :param amount: количество
        :return: None
        """
        self.player_inventory.sold_item(item, amount)


# В дальнейшем можно расширять функционал в лавке торговца,
# наследуясь от него и добавляя другие классы с новыми методами, атрибутами и
# свойствами. Допустим можно добавить возможность продажи предметов другим
# игрокам, для этого потребуется класс — хранилище игроков с соответствующими
# инструментами.

# OnlineMerchantsShop(MerchantsShop):
#   def __init__(self, inventory: Inventory, players_list: PlayersManagement):
#       super().__init__(inventory)
#       self.layers_list = players_list

#   ...
#   Методы для класса PlayersManagement
#   ...


if __name__ == "__main__":
    # Write your solution here
    pass
