from datetime import datetime


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        result = f'{self.__class__.__name__}('
        for key, value in self.__dict__.items():
            result += f'{key}={value!r}, '
        return result[:-2] + ')'

    @property
    def name(self) -> str:
        """
        Метод возвращает название книги
        :return: Название книги
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Метод установки нового названия книги
        :param new_name: Новое название
        :return: Метод ничего не возвращает
        """
        self._name = self.check_new_name(new_name)

    def check_new_name(self, new_name: str) -> str:
        """
        Метод валидации нового название книги
        :param new_name: Новое название
        :raise: TypeError, если новое имя книги не соответствует строковому типу
        :return: Новое название
        """
        if not isinstance(new_name, str):
            raise TypeError('Имя должно быть строковым типом!')
        return new_name

    @property
    def author(self) -> str:
        return self._author


class AudioBook(Book):
    """
    Класс аудиокниги
    """

    def __init__(self, name: str, author: str, duration: int | float):
        super().__init__(name, author)
        self.validate_duration(duration)
        self.duration = duration

    def validate_duration(self, duration: int | float):
        """
        Проверка валидности значения параметра продолжительности книги
        :param duration: Продолжительность аудиокниги
        :raise: TypeError, если тип параметра продолжительности не соответствует типам int или float
        :return: Метод ничего не возвращает
        """
        if not isinstance(duration, int | float):
            raise TypeError

    @staticmethod
    def check_time() -> datetime:
        """
        Проверим-ка сколько сейчас времени...
        :return: Ничего не возвращает, печатает текущее время
        """
        current_datetime = datetime.now()
        print(current_datetime)
        return current_datetime

    @classmethod
    def check_book_type(cls, book) -> None:
        """
        Определение типа книги, бумажная или аудио
        :param book: Передаваемый на проверку класс
        :return: Метод ничего не возвращает, печатает тип книги
        """
        if book.duration:
            print('Это аудиокнига!')
        print('Бумажная книга!')


if __name__ == "__main__":
    # Write your solution here

    pass
