# Exercise 28: Classes and Objects
# Task: Create a basic class Car with properties and a method.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def get_description(self):
        return f"{self.brand} {self.model}"

if __name__ == "__main__":
    my_car = Car("Tesla", "Model S")
    print(f"My car: {my_car.get_description()}")
