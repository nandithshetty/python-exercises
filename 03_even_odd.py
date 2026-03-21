# Exercise 3: Even or Odd
# Task: Write a function to check if a given integer is even or odd.

def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    test_num = 42
    result = "Even" if is_even(test_num) else "Odd"
    print(f"{test_num} is {result}")
