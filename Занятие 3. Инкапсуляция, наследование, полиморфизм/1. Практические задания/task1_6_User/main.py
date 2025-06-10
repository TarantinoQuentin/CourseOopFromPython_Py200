class User:
    def __init__(self, username: str, password: str, address: str):
        self.username = username
        # TODO создайте приватные атрибуты для пароля и адреса

    @staticmethod
    def check_permission(role: str) -> bool:
        """Простая проверка роли для доступа к конфиденциальным данным"""
        # TODO если роль 'admin', то вернуть True

    def get_password(self, role: str) -> str:
        ...  # TODO провести проверку доступа по роли, если прошла, то вернуть пароль, если не прошел проверку, то вызвать исключение PermissionError с текстом 'Доступ запрещен'

    def get_address(self, role: str) -> str:
        if self.check_permission(role):
            return self.__address
        else:
            raise PermissionError("Доступ запрещен")


if __name__ == "__main__":
    user = User("ivan_ivan", "secret_password", "Санкт-Петербург")

    try:
        print(user.get_password("user"))  # Должна возникнуть ошибка
    except PermissionError as e:
        print(e)

    print(user.get_password("admin"))  # Должно вернуться "secret_password"
