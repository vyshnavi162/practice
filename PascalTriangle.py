def pascal_triangle(numRows):
    triangle = [[1] * (i + 1) for i in range(numRows)]
    
    for i in range(2, numRows):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    return triangle

numRows = int(input("Enter number of rows for Pascal's Triangle: "))

for row in pascal_triangle(numRows):
    print(row)