# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, __brand, model):
        self.__brand = __brand
        self.model = model

    def get_brand(self):   # must be indented inside class
        return self.__brand + " !"

    def full_name(self):   # must be indented inside class
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.brand)         # Tesla
print(my_tesla.get_brand())   # Tesla !
print(my_tesla.full_name())   # Tesla Model S


