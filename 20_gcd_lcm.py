# Exercise 20: GCD and LCM
# Task: Write functions to find the Greatest Common Divisor and Least Common Multiple of two integers.

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

if __name__ == "__main__":
    n1, n2 = 12, 18
    print(f"GCD of {n1} and {n2}: {find_gcd(n1, n2)}")
    print(f"LCM of {n1} and {n2}: {find_lcm(n1, n2)}")
