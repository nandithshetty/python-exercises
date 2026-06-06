# Exercise 42: Find Missing Number
# Task: Find the missing number in an array containing numbers 1 to n with one element missing.

def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

if __name__ == "__main__":
    test_arr = [1, 2, 4, 5, 6]  # Missing 3
    print("Missing number:", find_missing(test_arr, 6))
