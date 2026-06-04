# Exercise 41: Flatten List
# Task: Flatten a deeply nested list recursively.

def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

if __name__ == "__main__":
    nested_list = [1, [2, [3, 4], 5], 6]
    print("Flattened:", flatten(nested_list))
