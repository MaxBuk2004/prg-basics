def f(sentence):
    return sentence.replace(" ", "")

if __name__ == "__main__":
    print(f(f("integrated development environment")))
    print(f(f("A programming language is a system of notation for writing computer programs")))  