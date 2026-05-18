# Exercise 32: Decorators
# Task: Write a decorator function to print execution log info.

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        res = func(*args, **kwargs)
        print(f"Finished function: {func.__name__}")
        return res
    return wrapper

@log_execution
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Sophia")
