# Parent class
class Device:
    def __init__(self, brand, model):
        self._brand = brand        # Protected attribute (encapsulation)
        self._model = model

    def device_info(self):
        return f"{self._brand} {self._model}"

    def power_on(self):
        return f"{self.device_info()} is powering on..."


# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Inherit from parent class
        self.storage = storage
        self.battery = battery

    # Polymorphism: overriding the method
    def power_on(self):
        return f"{self.device_info()} (Smartphone) is booting with {self.battery}% battery."

    def take_photo(self):
        return f"{self.device_info()} takes a stunning photo! "

    def install_app(self, app_name):
        return f"Installing {app_name} on {self.device_info()}."


# Another child class inheriting from Device
class Laptop(Device):
    def __init__(self, brand, model, ram, processor):
        super().__init__(brand, model)
        self.ram = ram
        self.processor = processor

    # Polymorphism again
    def power_on(self):
        return f"{self.device_info()} (Laptop) is starting with {self.ram} RAM."

    def run_program(self, program):
        return f"{self.device_info()} is running {program} smoothly on {self.processor}."


# Creating objects
phone = Smartphone("Samsung", "Galaxy S25", "256GB", 85)
laptop = Laptop("Dell", "XPS 15", "16GB", "Intel i9")

# Using methods
print(phone.power_on())        # Polymorphism in action
print(phone.take_photo())
print(phone.install_app("Instagram"))

print(laptop.power_on())       # Polymorphism in action
print(laptop.run_program("Python IDE"))
