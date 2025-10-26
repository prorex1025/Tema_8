"""
Лабораторная работа 8 - Задание 5
Реализация полиморфизма с классами Shape, Rectangle и Circle
"""

class Shape:
    """
    Базовый класс Shape (Фигура)
    Определяет общий интерфейс для всех фигур
    """

    def area(self):
        """
        Метод для вычисления площади фигуры
        Должен быть переопределен в дочерних классах
        """
        raise NotImplementedError("Метод area() должен быть переопределен")

    def perimeter(self):
        """
        Метод для вычисления периметра фигуры
        Должен быть переопределен в дочерних классах
        """
        raise NotImplementedError("Метод perimeter() должен быть переопределен")

    def get_info(self):
        """Возвращает информацию о фигуре"""
        return f"Фигура: {self.__class__.__name__}"

class Rectangle(Shape):
    """
    Класс Rectangle (Прямоугольник) наследуется от Shape
    """

    def __init__(self, width, height):
        """
        Конструктор прямоугольника

        Args:
            width (float): ширина прямоугольника
            height (float): высота прямоугольника
        """
        self.width = width
        self.height = height

    def area(self):
        """Вычисляет площадь прямоугольника"""
        return self.width * self.height

    def perimeter(self):
        """Вычисляет периметр прямоугольника"""
        return 2 * (self.width + self.height)

    def get_info(self):
        """Возвращает информацию о прямоугольнике"""
        return f"{super().get_info()} | Ширина: {self.width} | Высота: {self.height}"

class Circle(Shape):
    """
    Класс Circle (Круг) наследуется от Shape
    """

    def __init__(self, radius):
        """
        Конструктор круга

        Args:
            radius (float): радиус круга
        """
        self.radius = radius

    def area(self):
        """Вычисляет площадь круга"""
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        """Вычисляет длину окружности (периметр круга)"""
        return 2 * 3.14159 * self.radius

    def get_info(self):
        """Возвращает информацию о круге"""
        return f"{super().get_info()} | Радиус: {self.radius}"

class Triangle(Shape):
    """
    Класс Triangle (Треугольник) наследуется от Shape
    Дополнительный класс для демонстрации полиморфизма
    """

    def __init__(self, side1, side2, side3):
        """
        Конструктор треугольника

        Args:
            side1, side2, side3 (float): стороны треугольника
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """Вычисляет площадь треугольника по формуле Герона"""
        s = self.perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        """Вычисляет периметр треугольника"""
        return self.side1 + self.side2 + self.side3

    def get_info(self):
        """Возвращает информацию о треугольнике"""
        return f"{super().get_info()} | Стороны: {self.side1}, {self.side2}, {self.side3}"

def print_shape_info(shape):
    """
    Универсальная функция для работы с любыми фигурами
    Демонстрация полиморфизма - один интерфейс для разных типов фигур

    Args:
        shape (Shape): объект фигуры
    """
    print(f"📐 {shape.get_info()}")
    print(f"   📏 Площадь: {shape.area():.2f}")
    print(f"   📐 Периметр: {shape.perimeter():.2f}")
    print("-" * 40)

# Демонстрация полиморфизма
if __name__ == "__main__":
    print("=== ПОЛИМОРФИЗМ С КЛАССАМИ ФИГУР ===")

    # Создаем массив различных фигур
    shapes = [
        Rectangle(5, 10),
        Circle(7),
        Triangle(3, 4, 5),
        Rectangle(8, 6),
        Circle(3.5)
    ]

    print("1. Информация о всех фигурах:")
    print("=" * 40)

    # Обрабатываем все фигуры единообразно благодаря полиморфизму
    for shape in shapes:
        print_shape_info(shape)

    # Дополнительная демонстрация полиморфного поведения
    print("2. Суммарная площадь всех фигур:")
    total_area = sum(shape.area() for shape in shapes)
    print(f"   📊 Общая площадь: {total_area:.2f}")

    print("\n3. Проверка типов и полиморфизма:")
    for shape in shapes:
        print(f"   {shape.__class__.__name__}: "
              f"является Shape - {isinstance(shape, Shape)}")

    print(f"\n4. Вызов методов через базовый класс:")
    for shape in shapes:
        # Все объекты обрабатываются как Shape, но вызываются их собственные методы
        shape_as_base = shape  # Тип Shape, но реальный тип сохраняется
        print(f"   {shape.__class__.__name__}: площадь = {shape_as_base.area():.2f}")