# Exercise 19: Leap Year Check
# Task: Write a function to check if a year is a leap year.

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    year = 2024
    print(f"Is {year} a leap year? {is_leap_year(year)}")
