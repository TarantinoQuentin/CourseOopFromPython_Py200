class GoodBankAccount:
    def __init__(self, account_number: str, initial_balance: float):
        self.account_number = account_number
        self._balance = initial_balance  # Инкапсулированный атрибут

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма депозита должна быть положительной")

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостаточно средств или некорректная сумма")

    def get_balance(self) -> float:
        return self._balance


if __name__ == "__main__":
    # -------- Пример хорошей инкапсуляции --------------

    # Создаем объект банковского счета
    account = GoodBankAccount("123456", 1000.0)

    # Попытка изменить баланс напрямую не работает
    # account._balance = 5000.0  # Это плохая практика, так делать нельзя

    # Правильный способ изменения баланса через метод депозита
    account.deposit(500.0)
    print(account.get_balance())  # 1500.0

    # Правильный способ снятия денег
    account.withdraw(200.0)
    print(account.get_balance())  # 1300.0

    # Попытка снять больше средств, чем доступно
    account.withdraw(2000.0)  # "Недостаточно средств или некорректная сумма"if __name__ == "__main__":
    pass
