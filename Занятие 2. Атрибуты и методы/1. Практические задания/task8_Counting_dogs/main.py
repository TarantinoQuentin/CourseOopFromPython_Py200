class Dog:
    # Классовый атрибут для хранения количества созданных объектов
    total_dogs = 0

    def __init__(self, name):
        self.name = name
        # Увеличиваем значение классового атрибута при создании нового объекта
        Dog.total_dogs += 1

    # Классовый метод для получения количества созданных объектов
    @classmethod
    def get_total_dogs(cls):
        return cls.total_dogs


if __name__ == "__main__":
    # Создаём несколько объектов класса Dog
    dog1 = Dog("Buddy")
    dog2 = Dog("Lucy")
    dog3 = Dog("Max")

    # Используем классовый метод для получения количества созданных объектов
    print(Dog.get_total_dogs())  # 3

    # Доступ к классовому атрибуту напрямую
    print(Dog.total_dogs)  # 3
