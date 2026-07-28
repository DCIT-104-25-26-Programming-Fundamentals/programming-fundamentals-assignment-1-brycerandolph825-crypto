# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols, name):
    print(f"Enter matrix {name}:")
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        row = [int(x) for x in row]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        line = ""
        for value in row:
            line += f"{value}\t"
        print(line)

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        result.append(new_row)
    return result

def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)
    return result

def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

def main():
    # PART A - Transpose
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols, "A")
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    # PART B - Addition
    print("\nEnter first matrix for addition:")
    r1 = int(input("Enter number of rows: "))
    c1 = int(input("Enter number of columns: "))
    m1 = read_matrix(r1, c1, "1")
    print("Enter second matrix for addition:")
    m2 = read_matrix(r1, c1, "2")
    print("\nSum Matrix:")
    print_matrix(add_matrices(m1, m2))

    # PART C - Multiplication
    print("\nEnter matrix A (for multiplication):")
    ra = int(input("Enter number of rows: "))
    ca = int(input("Enter number of columns: "))
    a = read_matrix(ra, ca, "A")
    print("Enter matrix B (for multiplication):")
    rb = int(input("Enter number of rows: "))
    cb = int(input("Enter number of columns: "))
    b = read_matrix(rb, cb, "B")
    if ca != rb:
        print("Error: columns of A must equal rows of B.")
    else:
        print("\nProduct Matrix:")
        print_matrix(multiply_matrices(a, b))

main()