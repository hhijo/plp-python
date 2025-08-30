# Parent class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclass must implement this method")


# Child classes
class Car(Vehicle):
    def move(self):
        return f"{self.name} is Driving"


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is Flying"


class Boat(Vehicle):
    def move(self):
        return f"{self.name} is Sailing"


class Bike(Vehicle):
    def move(self):
        return f"{self.name} is Pedaling"


# Create objects
car = Car("Tesla")
plane = Plane("Boeing 747")
boat = Boat("Titanic")
bike = Bike("Mountain Bike")

# Polymorphism in action: Same method name, different behaviors
vehicles = [car, plane, boat, bike]

for v in vehicles:
    print(v.move())
