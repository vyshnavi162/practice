def rotateMatrix(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()
    
    return matrix

n = int(input("Enter the size of the square matrix (n x n): "))
print("Enter the matrix row by row (space-separated values):")
matrix = [list(map(int, input().split())) for _ in range(n)]

rotated_matrix = rotateMatrix(matrix)
print("Rotated matrix by 90 degrees clockwise:")
for row in rotated_matrix:
    print(row)