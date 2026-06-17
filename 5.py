#5. Count Vowels

text = input("Enter text: ")

count = 0

text.lower()

for ch in text.lower():
    if ch in "aeiou":
        count += 1
        
print("Vowels: ",count)