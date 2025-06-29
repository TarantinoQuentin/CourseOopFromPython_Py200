class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author


class PaperBook(Book):
    """
    Класс бумажной книги
    """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.validate_pages(pages)
        self.pages = pages

    def validate_pages(self, pages: int):
        """
        Проверка валидности значения параметра страниц книги
        :param pages: количество страниц книги
        :return: None
        """
        if not isinstance(pages, int):
            raise TypeError

    def __str__(self):
        super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """
    Класс аудиокниги
    """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def validate_duration(self, duration: float):
        """
        Проверка валидности значения параметра продолжительности книги
        :param duration: продолжительность аудиокниги
        :return: None
        """
        if not isinstance(duration, float):
            raise TypeError

    def __str__(self):
        super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
