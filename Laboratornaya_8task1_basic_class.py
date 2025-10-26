"""
Лабораторная работа 8 - Задание 2
Добавление атрибутов и методов в класс Car
"""

class Car:
    """
    Класс Car с дополнительными атрибутами и методами

    Атрибуты:
        make (str): производитель
        model (str): модель
        year (int): год выпуска
        mileage (float): пробег в км
        is_running (bool): состояние двигателя
    """

    def __init__(self, make, model, year=2023):
        """
        Конструктор с дополнительными параметрами

        Args:
            make (str): производитель
            model (str): модель
            year (int): год выпуска (по умолчанию 2023)
        """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0.0      # Начальный пробег
        self.is_running = False # Двигатель выключен

    def start_engine(self):
        """Запуск двигателя автомобиля"""
        if not self.is_running:
            self.is_running = True
            print(f"🚗 {self.make} {self.model}: двигатель запущен")
        else:
            print(f"⚠️ {self.make} {self.model}: двигатель уже работает")

    def stop_engine(self):
        """Остановка двигателя автомобиля"""
        if self.is_running:
            self.is_running = False
            print(f"🚗 {self.make} {self.model}: двигатель остановлен")
        else:
            print(f"⚠️ {self.make} {self.model}: двигатель уже выключен")

    def drive(self, distance):
        """
        Метод для движения автомобиля

        Args:
            distance (float): расстояние в км
        """
        if self.is_running:
            self.mileage += distance
            print(f"🚗 {self.make} {self.model}: проехал(а) {distance} км")
            print(f"📊 Общий пробег: {self.mileage} км")
        else:
            print(f"❌ {self.make} {self.model}: сначала запустите двигатель!")

    def get_info(self):
        """Возвращает полную информацию об автомобиле"""
        status = "заведен" if self.is_running else "заглушен"
        return (f"Автомобиль: {self.make} {self.model} ({self.year} г.) | "
                f"Пробег: {self.mileage} км | Состояние: {status}")

# Демонстрация работы
if __name__ == "__main__":
    print("=== РАСШИРЕННЫЙ КЛАСС CAR С МЕТОДАМИ ===")

    # Создаем автомобиль
    my_car = Car("Toyota", "Corolla", 2022)

    # Работа с методами
    print(my_car.get_info())
    my_car.start_engine()
    my_car.drive(50)
    my_car.drive(30)
    my_car.stop_engine()

    print(f"\nИтоговая информация:")
    print(my_car.get_info())