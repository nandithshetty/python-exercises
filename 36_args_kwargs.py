# Exercise 36: *args and **kwargs
# Task: Create a function that accepts variable arguments and keyword arguments.

def display_info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

if __name__ == "__main__":
    display_info("Red", "Blue", country="Canada", year=2026)
