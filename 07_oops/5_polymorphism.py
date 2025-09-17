# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    total_Car = 0   # class variable

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_Car += 1   # increments whenever a new Car/ElectricCar is created

    def fuel_type(self):
        return "Petrol or Diesel"   # default for normal cars

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    # overriding the method
    def fuel_type(self):
        return "Electric charge"


# Polymorphism in action
car1 = Car("Toyota", "Fortuner")
car2 = ElectricCar("Tesla", "Model S", "85kWh")

print(car1.full_name(), "→ Fuel:", car1.fuel_type())     # 
print(car2.full_name(), "→ Fuel:", car2.fuel_type())     # 

# Show total cars created
print(f"\nTotal Cars Created: {Car.total_Car}")          # Total Cars Created: 2
