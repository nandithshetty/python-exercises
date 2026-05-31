# Exercise 39: Basic Calculator
# Task: Build a command-line calculator for addition, subtraction, multiplication, and division.

def calculate(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Error"
    return "Invalid"

if __name__ == "__main__":
    print("10 + 5 =", calculate("+", 10, 5))
    print("10 / 0 =", calculate("/", 10, 0))
