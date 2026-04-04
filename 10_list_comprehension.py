# Exercise 10: List Comprehension
# Task: Create a list of squares of even numbers using list comprehension.

def squares_of_evens():
    squares = [x**2 for x in range(10) if x % 2 == 0]
    return squares

if __name__ == "__main__":
    print("Squares of evens from 0-9:", squares_of_evens())
