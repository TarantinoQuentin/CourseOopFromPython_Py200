class MyClass:
    def __init__(self, value):
        self.value = value  # Открытый атрибут

    def my_method(self):  # Открытый метод
        return self.value


class MyClassProtected:
    def __init__(self, value):
        self._value = value  # Защищённый атрибут

    def _my_method(self):  # Защищённый метод
        return self._value


class MyClassPrivate:
    def __init__(self, value):
        self.__value = value  # Приватный атрибут

    def __my_method(self):  # Приватный метод
        return self.__value


if __name__ == "__main__":
    obj = MyClass(42)
    print(obj.value)  # Открытый доступ
    obj.value = 100   # Изменение атрибута
    print(obj.value)

    obj = MyClassProtected(42)
    print(obj._value)  # Можно получить доступ, но это нарушает соглашение
    obj._value = 100   # Возможное изменение, но не рекомендуется
    print(obj._value)

    obj = MyClassPrivate(42)
    # print(obj.__value)  # Ошибка, доступ невозможен напрямую
    # obj.__my_method()   # Ошибка, доступ невозможен напрямую

    # Однако, есть обходной путь (механизм манглинга):
    print(obj._MyClassPrivate__value)  # Доступ возможен через манглинг имен, но это очень не рекомендуется
