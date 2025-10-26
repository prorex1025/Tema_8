"""
Лабораторная работа 8 - Задание 4
Реализация инкапсуляции в классе Car
"""

class Car:
    """
    Класс Car с инкапсулированными атрибутами

    Атрибуты:
        _make (str): защищенный атрибут производителя
        __model (str): приватный атрибут модели
        __vin (str): приватный VIN-номер
    """

    def __init__(self, make, model, vin):
        """
        Конструктор с инкапсулированными атрибутами

        Args:
            make (str): производитель
            model (str): модель
            vin (str): VIN-номер автомобиля
        """
        self._make = make          # Защищенный атрибут (одно подчеркивание)
        self.__model = model       # Приватный атрибут (два подчеркивания)
        self.__vin = vin           # Приватный VIN-номер
        self.__mileage = 0         # Приватный пробег
        self._is_running = False   # Защищенный статус двигателя

    # Публичные методы для доступа к приватным данным
    def get_model(self):
        """Публичный метод для получения модели"""
        return self.__model

    def get_vin(self):
        """Публичный метод для получения VIN (только частично)"""
        # Показываем только часть VIN для безопасности
        return f"***{self.__vin[-6:]}"

    def get_mileage(self):
        """Публичный метод для получения пробега"""
        return self.__mileage

    def set_mileage(self, new_mileage):
        """
        Публичный метод для установки пробега с проверкой

        Args:
            new_mileage (float): новый пробег
        """
        if new_mileage >= self.__mileage:
            self.__mileage = new_mileage
            print(f"📊 Пробег обновлен: {new_mileage} км")
        else:
            print("❌ Ошибка: пробег не может уменьшаться!")

    # Методы управления автомобилем
    def start_engine(self):
        """Запуск двигателя"""
        self._is_running = True
        print(f"🚗 {self._make} {self.__model}: двигатель запущен")

    def stop_engine(self):
        """Остановка двигателя"""
        self._is_running = False
        print(f"🚗 {self._make} {self.__model}: двигатель остановлен")

    def drive(self, distance):
        """
        Метод для движения автомобиля с обновлением пробега

        Args:
            distance (float): расстояние в км
        """
        if self._is_running:
            new_mileage = self.__mileage + distance
            self.set_mileage(new_mileage)
            print(f"🚗 Проехали {distance} км")
        else:
            print("❌ Сначала запустите двигатель!")

    def get_info(self):
        """Публичный метод для получения информации об автомобиле"""
        status = "заведен" if self._is_running else "заглушен"
        return (f"Автомобиль: {self._make} {self.__model} | "
                f"VIN: {self.get_vin()} | "
                f"Пробег: {self.__mileage} км | "
                f"Состояние: {status}")

# Демонстрация инкапсуляции
if __name__ == "__main__":
    print("=== ИНКАПСУЛЯЦИЯ В КЛАССЕ CAR ===")

    # Создаем автомобиль с инкапсулированными атрибутами
    my_car = Car("Toyota", "Corolla", "1HGBH41JXMN109186")

    # Работа с публичным интерфейсом
    print("1. Публичный интерфейс:")
    print(my_car.get_info())

    # Доступ к защищенному атрибуту (не рекомендуется, но возможно)
    print(f"\n2. Защищенный атрибут (_make): {my_car._make}")

    # Попытка доступа к приватным атрибутам
    try:
        print(my_car.__model)  # Вызовет AttributeError
    except AttributeError as e:
        print(f"❌ Ошибка доступа к __model: {e}")

    try:
        print(my_car.__vin)    # Вызовет AttributeError
    except AttributeError as e:
        print(f"❌ Ошибка доступа к __vin: {e}")

    # Правильный доступ через публичные методы
    print(f"\n3. Правильный доступ через геттеры:")
    print(f"Модель: {my_car.get_model()}")
    print(f"VIN: {my_car.get_vin()}")
    print(f"Пробег: {my_car.get_mileage()} км")

    # Управление автомобилем
    print(f"\n4. Управление автомобилем:")
    my_car.start_engine()
    my_car.drive(150)
    my_car.drive(80)

    # Попытка некорректного изменения пробега
    print(f"\n5. Проверка защиты данных:")
    my_car.set_mileage(100)  # Попытка уменьшить пробег

    print(f"\n6. Итоговая информация:")
    print(my_car.get_info())