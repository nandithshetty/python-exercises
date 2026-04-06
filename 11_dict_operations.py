# Exercise 11: Dictionary Operations
# Task: Perform basic dictionary lookup, insertion, and key checks.

def dict_demo():
    student = {"name": "Alice", "age": 21, "major": "Computer Science"}
    student["gpa"] = 3.8
    print("Student Profile:", student)
    
    if "age" in student:
        print(f"Student Age: {student['age']}")

if __name__ == "__main__":
    dict_demo()
