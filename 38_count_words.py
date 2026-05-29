# Exercise 38: Word Frequency Counter
# Task: Count the frequency of each word in a paragraph.

def count_words(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word:
            freq[clean_word] = freq.get(clean_word, 0) + 1
    return freq

if __name__ == "__main__":
    sample = "Python is simple. Python is powerful."
    print("Frequencies:", count_words(sample))
