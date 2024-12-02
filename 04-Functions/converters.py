def m_to_cm(n):
    """Convert meters to centimeters."""
    return n * 100

def cm_to_m(n):
    """Convert centimeters to meters."""
    return n / 100

def cm_to_inches(n):
    """Convert centimeters to inches."""
    return n / 2.54

def feet_and_inches_to_cm(feet, inches):
    """Convert feet and inches to centimeters."""
    total_inches = (feet * 12) + inches
    return total_inches * 2.54

if __name__ == "__main__":
    print(f'2m = {m_to_cm(2)} cm')
    print(f'532 cm = {cm_to_m(532)} m')
    print(f'532 cm = {cm_to_inches(532)} inches')
    print(f'5 feet 6 inches = {feet_and_inches_to_cm(5, 6)} cm')