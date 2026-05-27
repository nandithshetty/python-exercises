# Exercise 37: Merge Dictionaries
# Task: Write a function to merge two dictionaries (handling key overlaps).

def merge_dicts(d1, d2):
    res = d1.copy()
    res.update(d2)
    return res

if __name__ == "__main__":
    dict_a = {"x": 1, "y": 2}
    dict_b = {"y": 20, "z": 30}
    print("Merged:", merge_dicts(dict_a, dict_b))
