# Exercise 33: Generators
# Task: Create a generator function that yields squares of numbers up to limit.

def square_generator(limit):
    for i in range(1, limit + 1):
        yield i**2

if __name__ == "__main__":
    for sq in square_generator(5):
        print(sq)
