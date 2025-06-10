import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """
    # TODO определить конструктор

    # TODO перегрузить метод area, чтобы он возвращал площадь, но не терял родительский функционал


class Circle(Figure):
    """ Производный класс. Круг. """
    # TODO определить конструктор

    # TODO перегрузить метод area, чтобы он возвращал площадь,
но не терял родительский функционал"


if __name__ == "__main__":
    fig = Figure()
    print(fig.area())

    rect = Rectangle(5, 10)
    print(rect.area())

    circle = Circle(5)
    print(circle.area())
