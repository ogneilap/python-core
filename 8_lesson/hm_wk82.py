# Завдання 2: Абстракція

# Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний метод "обчислити_площу" 
# (calculate_area).

# Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" 
# (Triangle). У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.

# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.

from abc import ABC, abstractmethod
import math

class Shape:
    
    @classmethod
    @abstractmethod
    def calcilate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius= radius
        
    def calcilate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    
    def __init__(self, weight, height):
        self.weight= weight
        self.height = height
    
    def calcilate_area(self):
        return self.weight * self.height

class Triangle(Shape):
    
    def __init__(self, side1, side2,side3):
        self.side1= side1
        self.side2 = side2
        self.side3 = side3
        
    def calcilate_area(self):
        perimeter_2 = (self.side1+ self.side2 + self.side3)/2
        return math.sqrt(perimeter_2*(perimeter_2-self.side1)*(perimeter_2-self.side2)*(perimeter_2-self.side3))
    
circle = Circle(5)
rectangle = Rectangle(2, 3)
triangle = Triangle(3,4,5)
print(circle.calcilate_area())
print(rectangle.calcilate_area())
print(triangle.calcilate_area())