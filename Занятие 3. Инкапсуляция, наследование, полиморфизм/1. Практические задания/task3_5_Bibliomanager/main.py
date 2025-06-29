import datetime
import json


class LibraryItem:
    """
    Базовый класс для библиотечных материалов
    """

    def __init__(self, title: str, author: str | None = None, publication_year: int | None = None):
        """
        title - Название книги
        author - Автор
        publication_year - Год публикации
        """
        self.__validate_title(title)
        self.__title = title

        self.__validate_author(author)
        self.__author = author

        self.__validate_publication_year(publication_year)
        self.__publication_year = publication_year

        self.__is_checked_out = False

    @staticmethod
    def __validate_title(title: str):
        """
        Проверка на соответствие типу str, иначе ошибка TypeError
        """
        if not isinstance(title, str):
            raise TypeError

    @staticmethod
    def __validate_author(author: str):
        """
        Проверка на соответствие типу str или None, иначе ошибка TypeError
        """
        if not isinstance(author, (str, type(None))):
            raise TypeError

    @staticmethod
    def __validate_publication_year(year: int):
        """
        Проверка на соответствие типу int или None, иначе ошибка TypeError
        Если значение отрицательное или 0, то ошибка ValueError
        """
        if not isinstance(year, (int, type(None))):
            raise TypeError
        if year < 0:
            raise ValueError

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            print(f"{self.__title} было успешно выдано.")
        else:
            raise ValueError(f"{self.__title} уже выдано.")

    def return_item(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            print(f"{self.__title} было успешно возвращено.")
        else:
            raise ValueError(f"{self.__title} не было выдано.")

    # добавьте свойство is_checked_out (на чтение). Возвращает "Выдано" если is_checked_out=True, иначе "Доступно"
    @property
    def is_checked_out(self):
        return 'Выдано' if self.__is_checked_out else 'Доступно'

    # добавьте свойство title (на чтение)
    @property
    def title(self):
        return self.__title

    # добавьте свойство author (на чтение)
    @property
    def author(self):
        return self.__author

    # добавьте свойство publication_year (на чтение)
    @property
    def publication_year(self):
        return self.__publication_year

    def __str__(self):
        return f"'{self.__title}' от {self.__author} ({self.__publication_year}) — {self.is_checked_out}"

    def get_info(self):
        return None


class Book(LibraryItem):
    """
    Класс для книг
    """

    def __init__(self, title: str, author: str, genre: str, publication_year: int | None = None):
        """
        genre - Жанр
        """
        # Инициализируйте переменные от LibraryItem и добавьте новый приватный атрибут genre. Не забудьте, что нужна валидация перед записью
        super().__init__(title, author, publication_year)
        self.__validate_genre(genre)
        self.__genre = genre


    @staticmethod
    def __validate_genre(genre: str):
        """
        Проверка на соответствие типу str, иначе ошибка TypeError
        """
        if not isinstance(genre, str):
            raise TypeError

    # добавьте свойство genre (на чтение)
    @property
    def genre(self):
        return self.__genre

    # переопределите метод get_info, чтобы он отображал информацию специфичную для книги (Книга: 'Название книги', Автор: 'Кто написал', Жанр: 'Жанр книги', Год издания: 'Год')
    def get_info(self):
        return f'Книга: {self.title!r}, Автор: {self.author}, Жанр: {self.genre}, Год издания: {self.publication_year}'



class Magazine(LibraryItem):
    """
    Класс для журналов
    """

    def __init__(self, title, publication_year, issue_number):
        """
        issue_number - Номер выпуска
        """
         # Инициализируйте переменные от LibraryItem и добавьте новый приватный атрибут issue_number. Не забудьте, что нужна валидация перед записью
        super().__init__(title=title, publication_year=publication_year)
        self.__validate_issue_number(issue_number)
        self.__issue_number = issue_number

    @staticmethod
    def __validate_issue_number(issue_number: int):
        """
        Проверка на соответствие типу int, иначе ошибка TypeError
        """
        # написать метод валидации
        if not isinstance(issue_number, int):
            raise TypeError

    # добавьте свойство issue_number (на чтение)
    @property
    def issue_number(self):
        return self.__issue_number

    # переопределите метод get_info, чтобы он отображал информацию специфичную для журнала (Журнал: 'Название журнала', Номер выпуска: 'Номер', Год издания: 'Год')
    def get_info(self):
        return f'Журнал: {self.title!r}, Номер выпуска: {self.issue_number}, Год издания: {self.publication_year}'


class Newspaper(LibraryItem):
    """
    Класс для газет
    """

    # Инициализируйте переменные от LibraryItem и добавьте новый приватный атрибут publication_date. Не забудьте, что нужна валидация перед записью
    def __init__(self, title: str, publication_year: int, publication_date: str):
        super().__init__(title=title, publication_year=publication_year)
        self.__validate_publication_date(publication_date)
        self.__publication_date = publication_date

    @staticmethod
    def __validate_publication_date(publication_date: str):
        """
        Проверка на соответствие типу str, иначе ошибка TypeError
        Правильного формата разделения (день, месяц, и год должны быт разделены точкой '.', как пример: 01.01.2020)
        Проверка, что вообще дата существует в календаре (можно использовать datetime.date(day=1, month=1, year=2020),
            если не будет ошибок значит дата корректная)
        """
        # написать метод валидации
        if not isinstance(publication_date, str):
            raise TypeError('Неверное значение даты')
        if not '.' in publication_date:
            raise ValueError('Неверное значение даты')
        day, month, year = publication_date.split('.')
        datetime.date(day=int(day), month=int(month),year=int(year))

    # добавьте свойство publication_date (на чтение)
    @property
    def publication_date(self):
        return self.__publication_date

    # переопределите метод get_info, чтобы он отображал информацию специфичную для газеты (Газета: 'Название газеты', Дата выпуска: 'Дата', Год издания: 'Год')
    def get_info(self):
        return f'Газета: {self.title!r}, Дата выпуска: {self.publication_date}, Год издания: {self.publication_year}'


class LibraryManager:
    """
    Класс для управления библиотечными материалами
    """

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Метод для добавления элементов
        """
        if not isinstance(item, LibraryItem):
            raise TypeError("Объект должен быть экземпляром класса LibraryItem или его подклассов.")
        self.items.append(item)

    def check_out_item(self, title):
        """
        Метод для получения книги, у книги меняется флаг, что она была взята
        """
        for item in self.items:  # Поиск книги по названию
            if item.title == title:
                item.check_out()
                return
        raise ValueError(f"Материал с названием '{title}' не найден.")

    def return_item(self, title):
        """
        Метод для возвращения книги, у книги меняется флаг
        """
        for item in self.items:  # Поиск книги по названию
            if item.title == title:
                item.return_item()
                return
        raise ValueError(f"Материал с названием '{title}' не найден.")

    def list_items(self):
        """
        Отображение списка всех книг
        """
        column1_width = 100
        column2_width = 30
        print(f"|{'Материал':^{column1_width}}|{'Статус':^{column2_width}}|")
        print(f"|{'':-<{column1_width}}|{'':-<{column2_width}}|")
        for item in self.items:
            print(f"|{item.get_info():{column1_width}}|{item.is_checked_out:^{column2_width}}|")
        print(f"|{'':-<{column1_width}}|{'':-<{column2_width}}|")

    def search_by_title(self, title):
        """
        Метод поиска по вхождению названия
        """
        count = 0
        for item in self.items:
            if title.lower() in item.title.lower():
                print(item.get_info())
                count += 1
        if not count:
            print(f"Материала с названием '{title}' не найдено.")


if __name__ == "__main__":
    # Считывание данных книг для записи в библиотеку
    with open('library_items.json', encoding="utf-8") as file:
        books = json.load(file)

    # Создаем менеджер библиотеки
    library_manager = LibraryManager()

    # Добавляем материалы в библиотеку
    for data_book in books:
        if data_book['type'] == 'Книга':
            library_manager.add_item(Book(title=data_book['title'],
                                          author=data_book['author'],
                                          genre=data_book['genre'],
                                          publication_year=data_book['publication_year']))
        elif data_book['type'] == 'Журнал':
            library_manager.add_item(Magazine(title=data_book['title'],
                                              issue_number=data_book['issue_number'],
                                              publication_year=data_book['publication_year']))
        elif data_book['type'] == 'Газета':
            library_manager.add_item(Newspaper(title=data_book['title'],
                                               publication_date=data_book['publication_date'],
                                               publication_year=data_book['publication_year']))

    # Отображаем все доступные материалы
    print("Доступные материалы:")
    library_manager.list_items()

    # Поиск по названию
    print("\nПоиск книги '1984':")
    library_manager.search_by_title("1984")

    # Выдача материала
    print("\nВыдача книги '1984':")
    library_manager.check_out_item("1984")
    library_manager.list_items()

    # Попытка снова выдать ту же книгу
    print("\nПопытка снова выдать книгу '1984':")
    try:
        library_manager.check_out_item("1984")
    except ValueError as e:
        print(e)

    # Возвращение книги
    print("\nВозвращение книги '1984':")
    library_manager.return_item("1984")
    library_manager.list_items()
