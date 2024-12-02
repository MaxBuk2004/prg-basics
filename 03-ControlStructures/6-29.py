for i in range(1, 8):
    for j in range(1, 8):
        y = 7
        value = i + (j - 1) * y
        print(f'{value}', end=' ')
    print()