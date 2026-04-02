# Exercise 9: List Operations
# Task: Perform basic list manipulations (append, pop, slice, sort).

def list_demo():
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    print("After append:", fruits)
    
    fruits.pop(1)
    print("After pop:", fruits)
    
    fruits.sort()
    print("After sort:", fruits)

if __name__ == "__main__":
    list_demo()
