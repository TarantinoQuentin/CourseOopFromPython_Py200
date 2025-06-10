class Ink:
    def __init__(self, color: str, level: float):
        """
        Инициализация чернил.

        :param color: Цвет чернил.
        :param level: Уровень чернил (в процентах).
        """
        self.color = color
        self.level = level

    def use(self, amount: float):
        """
        Использует определенное количество чернил.

        :param amount: Количество используемых чернил.
        """
        if amount > self.level:
            raise ValueError("Недостаточно чернил для использования.")
        self.level -= amount

    def refill(self):
        """
        Заправка чернил.
        """
        self.level = 100.0
        print("Чернила полностью заправлены")


class Refill:
    def __init__(self, ink: Ink, tip_size: float, consumption: float = 0.1):
        """
        Инициализация стержня.

        :param ink: Объект Ink, представляющий чернила.
        :param tip_size: Размер наконечника (в мм).
        :param consumption: Расход чернил.
        """
        self.ink = ink
        self.tip_size = tip_size
        self.consumption = consumption

    def write(self, text: str):
        """
        Симулирует процесс письма и использует чернила.

        :param text: Текст для написания.
        """
        ink_usage = len(text) * self.tip_size * self.consumption
        self.ink.use(ink_usage)
        print(text)


class Pen:
    def __init__(self, brand: str, model: str, refill: Refill):
        """
        Инициализация ручки.

        :param brand: Бренд ручки.
        :param model: Модель ручки.
        :param refill: Объект Refill, представляющий стержень ручки.
        """
        self.brand = brand
        self.model = model
        self.refill = refill

    def write(self, text: str):
        """
        Симулирует процесс письма с использованием ручки.

        :param text: Текст для написания.
        """
        self.refill.write(text)

    def change_refill(self, new_refill: Refill):
        """
        Замена стержня в ручке.

        :param new_refill: Новый объект Refill для замены.
        """
        self.refill = new_refill


if __name__ == "__main__":
    # Создаем объект Ink
    blue_ink = Ink(color="blue", level=100.0)

    # Создаем объект Refill с чернилами и размером наконечника
    refill = Refill(ink=blue_ink, tip_size=0.5)

    # Создаем объект Pen с брендом, моделью и стержнем
    my_pen = Pen(brand="Parker", model="Jotter", refill=refill)

    # Используем ручку для письма
    print(f"Запас чернил {my_pen.refill.ink.level}")
    my_pen.write("Hello, world!")
    print(f"Запас чернил {my_pen.refill.ink.level}")

    # Заправляем чернила и снова используем ручку
    my_pen.refill.ink.refill()
    print(f"Запас чернил {my_pen.refill.ink.level}")
    my_pen.write("Writing with a newly refilled pen!")
    print(f"Запас чернил {my_pen.refill.ink.level}")
