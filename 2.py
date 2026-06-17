#Ask the user for a number and print whether it's even or odd.

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

largest = num1

if num2> largest:
    largest = num2
if num3> largest:
    largest = num3
    
print("Largest: ",largest)
