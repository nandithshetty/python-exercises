# Exercise 29: Class Inheritance
# Task: Implement inheritance with a subclass ElectricCar inheriting from Car.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type
        
    def describe(self):
        return f"{self.brand} {self.bike_type} Bike"

if __name__ == "__main__":
    my_bike = Bike("Yamaha", "Sport")
    print(my_bike.describe())
