import unittest

class BankAccount:
    """
    Базовый класс для банковского счета
    """
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if not amount > 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.__balance += amount
        print(f"Добавлено {amount}. Новый баланс: {self.__balance}")

    def withdraw(self, amount):
        if not 0 < amount <= self.__balance:
            raise ValueError('Недостаточно средств или неверная сумма.')
        self.__balance -= amount
        print(f"Выведено {amount}. Новый баланс: {self.__balance}")

    def __str__(self):
        return f"Баланс: {self.__balance} класса {self.__class__.__name__}"

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def _set_balance(self, new_balance):
        self.__balance = new_balance


class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        account = BankAccount('12345', 1000)
        # TODO проверьте что в атрибут баланса всё верно записалось

    def test_deposit_positive_amount(self):
        account = BankAccount('12345', 1000)
        # TODO добавьте 500 единиц к балансу и проверьте что в атрибут баланса всё верно записалось

    def test_deposit_negative_amount(self):
        account = BankAccount('12345', 1000)
        # TODO проверьте что вызывается ошибка при добавлении отрицательного баланса

    def test_withdraw_sufficient_funds(self):
        account = BankAccount('12345', 1000)
        # TODO снимите 500 единиц и проверьте что в атрибут баланса всё верно записалось

    def test_withdraw_insufficient_funds(self):
        account = BankAccount('12345', 1000)
        # TODO проверьте, что нельзя снять 1500 единиц со счета

    def test_withdraw_zero_or_negative_amount(self):
        account = BankAccount('12345', 1000)
        # TODO проверьте, что нельзя снять 0 со счета

    def test_account_number(self):
        account = BankAccount('12345', 1000)
        # TODO  проверьте доступность получения номера аккаунта


if __name__ == '__main__':
    unittest.main()