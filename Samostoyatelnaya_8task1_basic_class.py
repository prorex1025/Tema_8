"""
Задание 2: Добавление атрибутов и методов
Расширяем класс SmartDevice дополнительными возможностями
"""

class SmartDevice:
    """Класс умных устройств с расширенными возможностями"""

    def __init__(self, device_name, device_type, location, power_consumption=0):
        """
        Конструктор класса с дополнительными атрибутами

        Args:
            device_name (str): Название устройства
            device_type (str): Тип устройства
            location (str): Местоположение
            power_consumption (float): Потребляемая мощность в ваттах
        """
        self.device_name = device_name
        self.device_type = device_type
        self.location = location
        self.power_consumption = power_consumption
        self.is_online = True
        self.is_active = False  # Состояние устройства (вкл/выкл)
        self.usage_hours = 0    # Время использования в часах

    def turn_on(self):
        """Включить устройство"""
        if self.is_online:
            self.is_active = True
            print(f"🔌 {self.device_name} включен(а)")
        else:
            print(f"⚠️ {self.device_name} не в сети!")

    def turn_off(self):
        """Выключить устройство"""
        self.is_active = False
        print(f"🔌 {self.device_name} выключен(а)")

    def simulate_usage(self, hours):
        """Симулировать использование устройства в течение указанных часов"""
        if self.is_active:
            self.usage_hours += hours
            energy_used = self.power_consumption * hours
            print(f"⏱️ {self.device_name} использовался(ась) {hours} ч.")
            print(f"⚡ Потреблено энергии: {energy_used} Вт·ч")
            return energy_used
        else:
            print(f"⚠️ {self.device_name} выключен(а)!")
            return 0

    def get_status(self):
        """Получить полный статус устройства"""
        status = "🟢 онлайн" if self.is_online else "🔴 офлайн"
        state = "🔛 включен(а)" if self.is_active else "🔴 выключен(а)"
        return (f"{self.device_name} | {self.device_type} | "
                f"{self.location} | {status} | {state} | "
                f"Использовано: {self.usage_hours} ч.")

# Демонстрация работы
if __name__ == "__main__":
    print("=== ДЕМОНСТРАЦИЯ АТРИБУТОВ И МЕТОДОВ ===\n")

    # Создаем умные устройства
    lamp = SmartDevice("Умная лампа", "освещение", "гостиная", 15)
    heater = SmartDevice("Обогреватель", "климат", "спальня", 2000)

    # Работа с устройствами
    print("Управление устройствами:")
    lamp.turn_on()
    heater.turn_on()

    print("\nСимуляция использования:")
    lamp.simulate_usage(3)
    heater.simulate_usage(2)

    print("\nСтатусы устройств:")
    print(lamp.get_status())
    print(heater.get_status())

    print(f"\nОбщее время использования лампы: {lamp.usage_hours} ч.")