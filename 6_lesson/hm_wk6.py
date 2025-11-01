#1
class Animal:
    
    def __init__(self, name,species,age):
        self.name = name
        self.species = species
        self.age = age
        
    def make_sound(self):
        if self.species == "Dog":
            print("Gawww")
        elif self.species == "Cat":
            print("MMaaayyy")
        
cat = Animal("Dasha","Cat",18)
dog = Animal("Ralfa", "Dog", 8)
dog.make_sound()
cat.make_sound()


#2
class Rectangle:
    
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
litle = Rectangle(1,0.5)
bbig = Rectangle(100, 22)
print(litle.calculate_area())
print(bbig.calculate_area())
print(getattr(litle, 'heigh',"nima"))
print(bbig.__dict__)
print(litle.__doc__)

