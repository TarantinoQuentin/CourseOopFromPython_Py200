### Как наследуются защищенные и приватные атрибуты?

Наследование защищенных и приватных атрибутов в Python имеет свои особенности, 
которые необходимо учитывать при разработке классов.

Защищенные атрибуты обозначаются одним подчеркиванием (`_`) перед именем атрибута. 
Они не предназначены для прямого использования вне класса или его подклассов, но `могут быть унаследованы и использованы` в подклассах.


Приватные атрибуты обозначаются двумя подчеркиваниями (`__`) перед именем атрибута. 
Они предназначены для внутреннего использования в классе и не должны быть доступны вне его.


```python
class Parent:
    public_class_attr = 0
    _protected_class_attr = 1
    __private_class_attr = 2

    def __init__(self):
        self.public_attr = 3
        self._protected_attr = 4
        self.__private_attr = 5


class Child(Parent):
    def get_public_class_attr(self):
        return self.public_class_attr

    def get_protected_class_attr(self):
        return self._protected_class_attr

    def get_private_class_attr(self):
        return self.__private_class_attr

    def get_public_attr(self):
        return self.public_attr

    def get_protected_attr(self):
        return self._protected_attr

    def get_private_attr(self):
        return self.__private_attr


if __name__ == "__main__":
    child = Child()

    print(child.get_public_class_attr())  # 0
    print(child.get_protected_class_attr())  # 1

    try:
        print(child.get_private_class_attr())
    except AttributeError as err:
        print(err)  # 'Child' object has no attribute '_Child__private_class_attr'

    print(child.get_public_attr())  # 3
    print(child.get_protected_attr())  # 4

    try:
        print(child.get_private_attr())
    except AttributeError as err:
        print(err)  # 'Child' object has no attribute '_Child__private_attr'
```

Как видно публичные и защищенные атрибуты свободно наследуются, тоже касается и методов, однако приватные 
атрибуты и методы не наследуются напрямую. Если публичные и защищенные атрибуты и методы копируются при наследовании, то приватные остаются с тем классом, где 
были созданы первоначально, в этом и есть смысл приватности.

Вы можете перетранслировать значение через метод, если это необходимо, но это всегда будет значение первоисточника.


```python
class Parent:
    __private_class_attr = 2

    def __init__(self):
        self.__private_attr = 'Parent'

    def get_private_attr(self):
        return self.__private_attr

    @classmethod
    def get_private_class_attr(cls):
        return cls.__private_class_attr


class Child(Parent):
    def get_private_child_attr(self):
        return self.__private_attr

    @classmethod
    def get_private_class_child_attr(cls):
        return cls.__private_class_attr


if __name__ == "__main__":
    child = Child()

    print(child.get_private_class_attr())  # 2
    try:
        print(child.get_private_class_child_attr())
    except AttributeError as err:
        print(err)

    print(child.get_private_attr())  # Parent

    try:
        print(child.get_private_child_attr())
    except AttributeError as err:
        print(err)
```

Что есть в данном коде? В данном коде созданы методы в классе Parent и методы в классе Child. И те и те возвращают
приватные атрибуты экземплярные и классовые, но как видно через наследование и методы можно получить доступ к приватному атрибуту
родителя, но вот у дочернего не создается приватного атрибута, как по примеру защищенного. 

Приватные атрибуты или методы чаще всего используются если необходимо гарантировать, что атрибуты или методы класса 
не будут случайно изменены или использованы в подклассах или извне.

*Как пример*

```python
class APIClient:
    def __init__(self, api_key):
        self.__api_key = api_key  # Приватный атрибут для хранения ключа API

    def connect(self):
        self.__authenticate()
        print("Соединение установлено")

    def __authenticate(self):
        # Приватный метод для выполнения аутентификации
        print(f"Аутентификация с API ключом: {self.__api_key}")
```

Здесь метод `__authenticate` является приватным, чтобы его нельзя было переопределить в наследуемых классах. 
Это важно для сохранения целостности процесса подключения к API.
