# Exercise 15: Remove Duplicates
# Task: Write a function to remove duplicate elements from a list preserving order.

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5, 1]
    print(f"Original: {numbers}")
    print(f"Unique: {remove_duplicates(numbers)}")
