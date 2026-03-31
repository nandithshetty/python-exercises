# Exercise 8: Palindrome Check
# Task: Write a function to check if a string is a palindrome.

def is_palindrome(s):
    clean_s = "".join(s.split()).lower()
    return clean_s == clean_s[::-1]

if __name__ == "__main__":
    text = "A man a plan a canal Panama"
    print(f"Is '{text}' a palindrome? {is_palindrome(text)}")
