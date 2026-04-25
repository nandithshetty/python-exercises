# Exercise 21: Matrix Addition
# Task: Write a program to add two 2D matrices of the same size.

def add_matrices(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

if __name__ == "__main__":
    X = [[1, 2], [3, 4]]
    Y = [[5, 6], [7, 8]]
    print("Result of addition:", add_matrices(X, Y))
