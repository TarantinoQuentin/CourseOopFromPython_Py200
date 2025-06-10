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


class SavingsAccount(BankAccount):
    """
    Класс для сберегательного счета
    """
    def apply_interest(self, rate):
        """
        rate — это процентная ставка (в десятичных дробях).
        Например, если процентная ставка 5%, то передается значение 0.05
        """
        ...  # TODO реализуйте метод


class CheckingAccount(BankAccount):
    """
    Класс для расчетного счета
    """
    __commission = 0.01  # комиссия 1%

    def withdraw(self, amount):
        """
        amount - сумма для вывода
        """
        ...  # TODO Реализуйте метод


if __name__ == "__main__":
    # Пример использования
    savings = SavingsAccount("SA123", 1000)
    checking = CheckingAccount("CA456", 1000)

    # Сберегательный счет: начисление процентов
    savings.apply_interest(0.05)  # 5% годовых
    print(savings.get_balance())  # 1050.0

    # Расчетный счет: снятие средств с комиссией
    checking.withdraw(100)
    print(checking.get_balance())  # 899.0
