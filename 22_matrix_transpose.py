# Exercise 22: Matrix Transpose
# Task: Write a program to transpose a matrix.

def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("Original:", matrix)
    print("Transposed:", transpose(matrix))
