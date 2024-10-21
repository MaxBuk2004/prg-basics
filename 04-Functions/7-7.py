from ifsum import f

def main():
    test_cases = [
        (3124, True),
        (3124, False),
        (20576, False),
        (20576, True),
        (13115, True)
    ]
    
    for number, is_even in test_cases:
        result = f(number, is_even)
        print(f'f({number}, {is_even}) returns {result}')

if __name__ == "__main__":
    main()