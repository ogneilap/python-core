# **Завдання 1: Наслідування**

# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:

# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)

# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.

# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. 
# Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. Наприклад, для класу `Car` 
# можна додати атрибут `fuel_type` та метод `start_engine()`.

# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.
# **Завдання 2: Поліморфізм**

# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб 
# (наприклад, "Це [виробник] [модель] [рік] року виробництва.").

# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.

# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте 
# за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model= model
        self.year =year
        
    def display_info(self):
        pass
        
class Car(Vehicle):
    
    def __init__(self, make, model, year,door):
        super().__init__(make, model, year)
        self.door = door
    def openWindow(self):
        print("Your car open window ")
        
    def display_info(self):
        return f"Це {self.make} {self.model} {self.year} року виробицтва з {self.door} дверима"
        
        
class Motorcycle(Vehicle):
    
    def __init__(self, make, model, year, type_mot):
        super().__init__(make, model, year)
        self.type_mot = type_mot
        
    def go_stant(self):
        print(f"{self.type_mot} stant")
    
    def display_info(self):
        return f"Це {self.type_mot} {self.make} {self.model} {self.year} року виробицтва "
        
porsh = Car("Porshe", "Panamera", 2023, 2)
syzyki = Motorcycle("Syzyki", "Ninja", 2004, "sport")

porsh.openWindow()
syzyki.go_stant()

print(porsh.__dict__)
print(syzyki.__dict__)

print(porsh.display_info())
print(syzyki.display_info())