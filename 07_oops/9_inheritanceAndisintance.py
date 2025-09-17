# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


# Object of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Checking inheritance relationships
print(isinstance(my_tesla, ElectricCar))   # True
print(isinstance(my_tesla, Car))           # True
print(isinstance(my_tesla, object))        # True (all classes inherit from object)
