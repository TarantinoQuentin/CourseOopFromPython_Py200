class User:
    def __init__(self, username: str, password: str, address: str):
        self.username = username
        self.__password = password
        self.__address = address

    @staticmethod
    def check_permission(role: str) -> bool:
        """Простая проверка роли для доступа к конфиденциальным данным"""
        if role == 'admin':
            return True
        return False

    def get_password(self, role: str) -> str:
        if self.check_permission(role):
            return self.__password
        raise PermissionError('Доступ запрещен')

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
