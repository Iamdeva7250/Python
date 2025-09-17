# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.


class Car:
    # Class variable
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1   # increment counter whenever a new car is created

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


# Objects
car1 = Car("Toyota", "Fortuner")
car2 = ElectricCar("Tesla", "Model S", "85kWh")
car3 = Car("Hyundai", "Creta")

print(car1.full_name(), "→ Fuel:", car1.fuel_type())
print(car2.full_name(), "→ Fuel:", car2.fuel_type())
print(car3.full_name(), "→ Fuel:", car3.fuel_type())

# Accessing class variable
print(f"\nTotal cars created: {Car.total_cars}")
