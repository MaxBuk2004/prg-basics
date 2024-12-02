array = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        array[i][j] = (i + 1) * (j + 1)

for row in array:
    print(" ".join(map(str, row)))