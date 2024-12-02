def f(name):
    words = name.split()
    acronym = ""
    for word in words:
        if word:
            first_letter = word[0].upper()
            acronym += first_letter
    
    return acronym

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))