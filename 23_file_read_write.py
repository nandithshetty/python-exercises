# Exercise 23: File Read and Write
# Task: Write a script to write text data to a file and read it back.

def file_io_demo():
    filename = "temp_notes.txt"
    with open(filename, "w") as f:
        f.write("Learning Python is fun!\nThis is a temporary file.\n")
        
    with open(filename, "r") as f:
        content = f.read()
        print("Read Content:\n" + content)
        
    if os.path.exists(filename):
        os.remove(filename)

if __name__ == "__main__":
    import os
    file_io_demo()
