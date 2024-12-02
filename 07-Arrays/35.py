def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))

matrices = [
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
    
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0],
     [5, 6, 7, 8, 9]]
]

for idx, matrix in enumerate(matrices, 1):
    print(f"Matrix {idx} before transposition:")
    display_matrix(matrix)
    
    transposed = transpose_matrix(matrix)
    
    print(f"\nMatrix {idx} after transposition:")
    display_matrix(transposed)
    print()