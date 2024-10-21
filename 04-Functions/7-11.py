def f(n):
    result = ""
    current = 1

    while current <= n:
        result += str(current)
        current += 1

    return result

if __name__ == "__main__":
    print(f'f(11) returns "{f(11)}"')
    print(f'f(4) returns "{f(4)}"')