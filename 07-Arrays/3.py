arr = [15, 8, 31, 47, 2, 19]

print("existed array:", " ".join(map(str, arr)))

reversed_arr = []

for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print("reverse array:", " ".join(map(str, reversed_arr)))