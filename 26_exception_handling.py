# Exercise 26: Exception Handling
# Task: Demonstrate robust try-except-finally blocks handling ZeroDivisionError.

def divide_safely(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    else:
        return result
    finally:
        print("Division check complete.")

if __name__ == "__main__":
    print("Result of 10 / 2:", divide_safely(10, 2))
    print("Result of 10 / 0:", divide_safely(10, 0))
