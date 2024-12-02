def f(x, y):
    count = 0

    for number in range(x, y + 1):
        if number < 0 and number % 2 == 0:
            count += 1
    
    return count

if __name__ == "__main__":
    print(f'f(-7, 8) returns {f(-7, 8)}')  # Should return 3
    print(f'f(-1, 11) returns {f(-1, 11)}')  # Should return 0