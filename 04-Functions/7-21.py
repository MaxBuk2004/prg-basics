def f(password):
    if len(password) < 6:
        return False
    
    unique_characters = set(password)
    if len(unique_characters) != len(password):
        return False
    
    return True

if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))