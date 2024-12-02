def f(palindrome):
    normalized = ''.join(filter(str.isalnum, palindrome)).lower()
    
    return normalized == normalized[::-1]

if __name__ == "__main__":
    print(f'f("radar") returns {f("radar")}')
    print(f'f("12-11-21") returns {f("12-11-21")}')
    print(f'f("book") returns {f("book")}')