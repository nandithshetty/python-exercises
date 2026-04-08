# Exercise 12: Anagram Check
# Task: Write a function to check if two strings are anagrams.

def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

if __name__ == "__main__":
    w1, w2 = "Listen", "Silent"
    print(f"Are '{w1}' and '{w2}' anagrams? {are_anagrams(w1, w2)}")
