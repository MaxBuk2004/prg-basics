array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

smallest = float('inf')
largest = float('-inf')
smallest_position = (-1, -1)
largest_position = (-1, -1)

for i in range(len(array)):
    for j in range(len(array[i])):
        value = array[i][j]
        
        if value < smallest:
            smallest = value
            smallest_position = (i, j)
        
        if value > largest:
            largest = value
            largest_position = (i, j)

print(f"Smallest value: {smallest} at row {smallest_position[0]} and column {smallest_position[1]}")
print(f"Largest value: {largest} at row {largest_position[0]} and column {largest_position[1]}")