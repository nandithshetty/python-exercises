# Exercise 6: Prime Number Check
# Task: Write a function to check if a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = 29
    print(f"Is {num} prime? {is_prime(num)}")
