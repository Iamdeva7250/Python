# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
# # 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return f"{self.brand} {self.model}"


class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery size: {self.battery_size}"


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def engine_info(self):
        return f"Engine power: {self.horsepower} HP"


# Multiple Inheritance
class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size, horsepower):
        Car.__init__(self, brand, model)         # initialize Car
        Battery.__init__(self, battery_size)     # initialize Battery
        Engine.__init__(self, horsepower)        # initialize Engine

    def fuel_type(self):   # overriding Car's method
        return "Electric charge"


# Object
my_tesla = ElectricCar("Tesla", "Model S", "85kWh", 670)

# Demonstration
print(my_tesla.full_name())          # Tesla Model S
print(my_tesla.fuel_type())          # Electric charge
print(my_tesla.battery_info())       # Battery size: 85kWh
print(my_tesla.engine_info())        # Engine power: 670 HP
