
class Book:
    def __init__(self, name, page, year):
        self.name = name
        self.page = page
        self.year = year

    def __repr__(self):
        # TODO сделайте так, чтобы __repr__ сам подстраивался под атрибуты что есть у него в классе


class EBook(Book):
    def __init__(self, name, page, year, size):
        super().__init__(name, page, year)
        self.size = size


class AudioBook(Book):
    def __init__(self, name, page, year, duration):
        super().__init__(name, page, year)
        self.duration = duration


if __name__ == "__main__":
    book = Book('Война и мир', 960, 1867)
    print(repr(book))  # Book(name='Война и мир', page=960, year=1867)

    ebook = EBook('Война и мир', 960, 1867, 100)
    print(repr(ebook))  # EBook(name='Война и мир', page=960, year=1867, size=100)
    # Если в __repr__ класса Book всё прописано верно, то __repr__ EBook переопределять будет не нужно

    abook = AudioBook('Война и мир', 960, 1867, 1000)
    print(repr(abook))  # AudioBook(name='Война и мир', page=960, year=1867, duration=1000)
