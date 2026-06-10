# Exercise 44: Binary-Decimal Converter
# Task: Write functions to convert a binary string to decimal and vice versa.

def bin_to_dec(b_str):
    return int(b_str, 2)

def dec_to_bin(n):
    return bin(n)[2:]

if __name__ == "__main__":
    b = "1101"
    d = 13
    print(f"Binary {b} to Decimal: {bin_to_dec(b)}")
    print(f"Decimal {d} to Binary: {dec_to_bin(d)}")
