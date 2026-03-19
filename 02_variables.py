# Exercise 2: Variables and Type Conversion
# Task: Declare variables of different types (int, float, string, bool) and convert them.

def variable_conversion():
    num_str = "100"
    num_int = int(num_str)
    num_float = float(num_int)
    
    print(f"String: {num_str} (Type: {type(num_str)})")
    print(f"Integer: {num_int} (Type: {type(num_int)})")
    print(f"Float: {num_float} (Type: {type(num_float)})")

if __name__ == "__main__":
    variable_conversion()
