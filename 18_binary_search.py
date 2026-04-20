# Exercise 18: Binary Search
# Task: Implement binary search on a sorted list.

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    sorted_items = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    print(f"Index of {target}: {binary_search(sorted_items, target)}")
