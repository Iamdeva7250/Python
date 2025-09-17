# # 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.


class Car:
    total_Car = 0   # class variable

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_Car += 1

    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return f"{self.brand} {self.model}"

    @staticmethod
    def general_description():
        return "Cars are a means of transport with wheels, typically powered by an engine."


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


# Objects
car1 = Car("Toyota", "Fortuner")
car2 = ElectricCar("Tesla", "Model S", "85kWh")

# Polymorphism
print(car1.full_name(), "→ Fuel:", car1.fuel_type())
print(car2.full_name(), "→ Fuel:", car2.fuel_type())

# Static method usage
print("\nGeneral Car Info:", Car.general_description())   # via class
print("General Car Info:", car1.general_description())   # via object
