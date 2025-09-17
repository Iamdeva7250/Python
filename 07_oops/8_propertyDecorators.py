# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model   # make model "private"
        Car.total_cars += 1

    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return f"{self.brand} {self.__model}"

    @property
    def model(self):
        """Read-only property for model"""
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


# Objects
car1 = Car("Toyota", "Fortuner")
car2 = ElectricCar("Tesla", "Model S", "85kWh")

print(car1.full_name())   # Toyota Fortuner
print(car2.full_name())   # Tesla Model S

# Access model (read-only)
print(car1.model)         # Fortuner

# Trying to modify will raise an error
try:
    car1.model = "Innova"   # ❌ not allowed
except AttributeError as e:
    print("Error:", e)

