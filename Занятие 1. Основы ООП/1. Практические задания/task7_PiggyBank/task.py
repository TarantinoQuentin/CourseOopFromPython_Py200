class Coin:
    def __init__(self, denomination: float):
        """
        Инициализация монеты.

        :param denomination: Номинал монеты.
        """
        self.denomination = denomination


class PiggyBank:
    def __init__(self):
        """
        Инициализация копилки.
        """
        self.coins = []
        self.is_broken = False

    def add_coin(self, coin: Coin):
        """
        Добавляет монету в копилку.

        :param coin: Объект Coin для добавления.
        """
        ...  # TODO реализуйте метод как в описании

    def break_piggy_bank(self):
        """
        Разбивает копилку и возвращает информацию о монетах.

        :return: Словарь, где ключ - номинал монеты, значение - количество монет этого номинала.
        """
        ...  # TODO реализуйте метод как в описании


if __name__ == "__main__":
    # Создаем копилку
    piggy_bank = PiggyBank()

    # Создаем несколько монет
    coin1 = Coin(1.0)
    coin2 = Coin(0.5)
    coin3 = Coin(0.25)
    coin4 = Coin(1.0)
    coin5 = Coin(0.5)

    # Добавляем монеты в копилку
    piggy_bank.add_coin(coin1)
    piggy_bank.add_coin(coin2)
    piggy_bank.add_coin(coin3)
    piggy_bank.add_coin(coin4)
    piggy_bank.add_coin(coin5)

    # Печатаем состояние копилки
    print(piggy_bank.coins)

    # Разбиваем копилку
    coins_info = piggy_bank.break_piggy_bank()
    print("Монеты в копилке:", coins_info)

    # Пытаемся добавить монету в разбитую копилку (должна быть ошибка)
    try:
        piggy_bank.add_coin(Coin(2.0))
    except ValueError as e:
        print(e)

    # Пытаемся снова разбить копилку (должна быть ошибка)
    try:
        piggy_bank.break_piggy_bank()
    except ValueError as e:
        print(e)
