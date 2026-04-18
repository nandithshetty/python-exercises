# Exercise 17: Linear Search
# Task: Implement linear search to find an element's index in a list.

def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1

if __name__ == "__main__":
    items = [10, 23, 45, 70, 11, 15]
    target = 70
    print(f"Index of {target}: {linear_search(items, target)}")
