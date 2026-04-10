# Exercise 13: Count Vowels
# Task: Write a function to count the number of vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    text = "Beautiful Day"
    print(f"Number of vowels in '{text}': {count_vowels(text)}")
