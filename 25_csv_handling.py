# Exercise 25: CSV Operations
# Task: Create a CSV string, parse it using the csv module, and print the rows.

import csv
import io

def csv_demo():
    csv_data = "Name,Age,Role\nCharlie,30,Developer\nDiana,25,Designer"
    f = io.StringIO(csv_data)
    reader = csv.reader(f)
    for row in reader:
        print(row)

if __name__ == "__main__":
    csv_demo()
