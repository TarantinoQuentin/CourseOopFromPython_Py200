class A:
    attr_A = 10

    def __init__(self, param_a):
        self.param_a = param_a

    def method_a(self):
        return 'A'


class B:
    attr_B = 20

    def __init__(self, param_b):
        self.param_b = param_b

    def method_b(self):
        return 'B'


class C(A, B):  # Множественное наследование
    attr_C = 30

    def method_c(self):
        return 'C'


if __name__ == "__main__":
    obj_c = C(30)  # def __init__ тоже скопировался, но с какого класса?

    print(obj_c.param_a)  # 30 Скопировался только __init__ с класса A, так как при одинаковых названиях оставляется
    # тот чей класс левее при наследовании
    try:
        print(obj_c.param_b)
    except AttributeError as err:
        print(err)  # 'C' object has no attribute 'param_b'

    # Остальные методы и атрибуты скопировались полностью, так как их названия не повторяются
    print(obj_c.method_a(), obj_c.method_b(), obj_c.method_c())  # A B C
    print(obj_c.attr_A, obj_c.attr_B, obj_c.attr_C)  # 10 20 30
