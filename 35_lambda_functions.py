# Exercise 35: Lambda, Map, Filter
# Task: Perform functional operations using lambda, map, and filter on a list.

def functional_demo():
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    doubled = list(map(lambda x: x * 2, numbers))
    
    print("Original:", numbers)
    print("Evens:", evens)
    print("Doubled:", doubled)

if __name__ == "__main__":
    functional_demo()
