# Exercise 40: Recursive Bubble Sort
# Task: Implement bubble sort recursively.

def bubble_sort_recursive(lst, n=None):
    if n is None:
        n = len(lst)
    if n == 1:
        return lst
        
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            
    return bubble_sort_recursive(lst, n - 1)

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    print("Sorted recursively:", bubble_sort_recursive(arr))
