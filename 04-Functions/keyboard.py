def input_string(message):
    return input(message)

def input_integer(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def input_real(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid real number.")

def input_boolean(message):
    while True:
        value = input(message).strip().lower()
        if value == 'y':
            return True
        elif value == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")
