def f(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

if __name__ == "__main__":
    print(f'f(5) returns {f(5)}')
    print(f'f(9) returns {f(9)}')