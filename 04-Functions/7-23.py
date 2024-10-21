def f(x, y):
    total_sum = 0

    for number in range(x, y):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total_sum += number

    return total_sum

if __name__ == "__main__":
    print(f(1, 20))
    print(f(10, 30)) 