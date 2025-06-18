class Dog:
    total_dogs = 0

    @classmethod
    def increment_total_dogs(cls, count=1):
        if count <= 0:  # Добавляем простую проверку
            raise ValueError("Ошибка: количество должно быть положительным")
        cls.total_dogs += count

    def __init__(self, name):
        self.name = name
        self.increment_total_dogs()


if __name__ == "__main__":
    # Создание объектов
    dog1 = Dog("Buddy")
    dog2 = Dog("Lucy")

    # Проверка количества
    print(Dog.total_dogs)  # 2
