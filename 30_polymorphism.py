# Exercise 30: Polymorphism
# Task: Create multiple classes showing method polymorphism.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal_obj):
    print(animal_obj.speak())

if __name__ == "__main__":
    make_animal_speak(Dog())
    make_animal_speak(Cat())
