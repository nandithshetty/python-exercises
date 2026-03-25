# Exercise 5: Fibonacci Sequence
# Task: Write a function to generate Fibonacci sequence up to n terms.

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

if __name__ == "__main__":
    terms = 10
    print(f"Fibonacci sequence (first {terms} terms): {fibonacci(terms)}")
