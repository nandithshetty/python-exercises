# Exercise 14: Largest Element in List
# Task: Write a function to find the maximum element in a list without using max().

def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == "__main__":
    nums = [12, 45, 2, 89, 34]
    print(f"Max value: {find_max(nums)}")
