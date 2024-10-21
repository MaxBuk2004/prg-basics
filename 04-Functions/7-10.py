def f(n):
    result = ""
    count = 0

    while count < n:
        result += "*"
        if count < n - 1:
            result += "/"
        count += 1

    return result

if __name__ == "__main__":
    print(f'f(4) returns "{f(4)}"')
    print(f'f(1) returns "{f(1)}"')
    print(f'f(0) returns "{f(0)}"') 