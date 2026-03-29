# Exercise 7: Reverse a String
# Task: Write a function to reverse a string.

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    text = "Python Programming"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
