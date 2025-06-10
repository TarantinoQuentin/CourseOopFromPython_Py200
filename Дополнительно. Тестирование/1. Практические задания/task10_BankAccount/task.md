Допишите unit тесты и проверьте работоспособность.

### Возможная реализация для проверки (полный код)

<div class="hint">

```python
class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        account = BankAccount('12345', 1000)
        self.assertEqual(account.get_balance(), 1000)

    def test_deposit_positive_amount(self):
        account = BankAccount('12345', 1000)
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

    def test_deposit_negative_amount(self):
        account = BankAccount('12345', 1000)
        with self.assertRaises(ValueError):
            account.deposit(-500)

    def test_withdraw_sufficient_funds(self):
        account = BankAccount('12345', 1000)
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 500)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount('12345', 1000)
        with self.assertRaises(ValueError):
            account.withdraw(1500)

    def test_withdraw_zero_or_negative_amount(self):
        account = BankAccount('12345', 1000)
        with self.assertRaises(ValueError):
            account.withdraw(0)

    def test_account_number(self):
        account = BankAccount('12345', 1000)
        self.assertEqual(account.get_account_number(), '12345')
```

</div>