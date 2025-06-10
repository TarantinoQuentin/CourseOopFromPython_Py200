class Vector:
    def __init__(self, x: int | float = 0, y: int | float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        ... # TODO реализуйте вычитание

    def __mul__(self, other):
        ... # TODO реализуйте умножение

    def __truediv__(self, other):
        ... # TODO реализуйте деление


if __name__ == "__main__":
    v1 = Vector(2, 1)
    v2 = Vector(1, 2)
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * v2)
    print(v1 / v2)



