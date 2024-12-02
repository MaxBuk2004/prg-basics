def identity_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))

sizes = [3, 5, 8]
for size in sizes:
    print(f"Identity Matrix of size {size}:")
    matrix = identity_matrix(size)
    display_matrix(matrix)
    print()