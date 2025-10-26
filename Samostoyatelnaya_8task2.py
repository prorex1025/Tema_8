"""
Задание 4: Реализация инкапсуляции
Защищаем внутренние данные классов с помощью инкапсуляции
"""

class SecureSmartDevice:
    """
    Класс с защищенными и приватными атрибутами
    Демонстрация инкапсуляции в ООП
    """

    def __init__(self, device_name, device_type, location, firmware_version="1.0"):
        """
        Конструктор с инкапсулированными атрибутами

        Args:
            device_name (str): Публичное название устройства
            device_type (str): Защищенный тип устройства
            location (str): Приватное местоположение
            firmware_version (str): Версия прошивки
        """
        self.device_name = device_name                    # Публичный атрибут
        self._device_type = device_type                   # Защищенный атрибут
        self.__location = location                        # Приватный атрибут
        self.__firmware_version = firmware_version        # Приватный атрибут
        self._is_online = True                           # Защищенный статус
        self.__security_key = "secure123"                # Приватный ключ безопасности

    # Публичные методы для доступа к приватным данным
    def get_location(self):
        """Публичный метод для получения местоположения"""
        return self.__location

    def set_location(self, new_location):
        """Публичный метод для изменения местоположения с проверкой"""
        if isinstance(new_location, str) and len(new_location) > 0:
            self.__location = new_location
            print(f"📍 Местоположение {self.device_name} изменено на: {new_location}")
        else:
            print("⚠️ Ошибка: неверное местоположение")

    def get_firmware_info(self):
        """Публичный метод для получения информации о прошивке"""
        return f"Версия прошивки: {self.__firmware_version}"

    def update_firmware(self, new_version):
        """Публичный метод для обновления прошивки"""
        if new_version > self.__firmware_version:
            self.__firmware_version = new_version
            print(f"🔄 {self.device_name}: прошивка обновлена до версии {new_version}")
        else:
            print("⚠️ Версия прошивки не может быть понижена")

    # Защищенные методы для внутренней логики
    def _connect_to_network(self):
        """Защищенный метод для подключения к сети"""
        self._is_online = True
        print(f"📶 {self.device_name} подключен к сети")

    def _disconnect_from_network(self):
        """Защищенный метод для отключения от сети"""
        self._is_online = False
        print(f"📶 {self.device_name} отключен от сети")

    # Публичный интерфейс
    def connect(self):
        """Публичный метод для подключения устройства"""
        self._connect_to_network()

    def disconnect(self):
        """Публичный метод для отключения устройства"""
        self._disconnect_from_network()

    def get_status(self):
        """Публичный метод для получения статуса"""
        status = "онлайн" if self._is_online else "офлайн"
        return (f"{self.device_name} | {self._device_type} | "
                f"{self.get_location()} | {status}")

# Демонстрация инкапсуляции
if __name__ == "__main__":
    print("=== ДЕМОНСТРАЦИЯ ИНКАПСУЛЯЦИИ ===\n")

    # Создаем защищенное устройство
    secure_device = SecureSmartDevice("Защищенная камера", "безопасность", "входная дверь", "2.1")

    # Работа с публичными методами
    print("Публичный интерфейс:")
    print(secure_device.get_status())
    secure_device.connect()

    # Доступ к защищенным атрибутам (не рекомендуется, но возможно)
    print(f"\nЗащищенный атрибут (_device_type): {secure_device._device_type}")

    # Попытка доступа к приватным атрибутам (вызовет ошибку)
    try:
        print(secure_device.__location)  # Это вызовет AttributeError
    except AttributeError as e:
        print(f"❌ Ошибка доступа к приватному атрибуту: {e}")

    # Правильный доступ через публичные методы
    print(f"\nПравильный доступ через геттер:")
    print(f"Местоположение: {secure_device.get_location()}")
    print(secure_device.get_firmware_info())

    # Изменение через сеттеры
    secure_device.set_location("задний двор")
    secure_device.update_firmware("2.2")

    print(f"\nОбновленный статус:")
    print(secure_device.get_status())

    # Демонстрация защиты данных
    print(f"\nПопытка неправильного обновления:")
    secure_device.update_firmware("1.0")  # Попытка понизить версию
    secure_device.set_location("")        # Пустое местоположение