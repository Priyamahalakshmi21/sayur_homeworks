'''
Program 1 - Write a program to print the following pattern.
Input is 5 for the following pattern.
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''
n = int(input("Enter a number : "))
matrix = []
for _ in range(2 * n - 1):
    row = [0] * (2 * n - 1)
    matrix.append(row)
for i in range(n):
    for j in range(i, 2 * n - 1 - i):
        matrix[i][j] = n - i
        matrix[j][i] = n - i
        matrix[j][2 * n - 2 - i] = n - i
        matrix[2 * n - 2 - i][j] = n - i
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
