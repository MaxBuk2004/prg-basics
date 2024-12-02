def f(detector):
    count = 0
    max_people = 0

    for action in detector:
        if action == '+':
            count += 1
        elif action == '-':
            count -= 1
        
        max_people = max(max_people, count)
    
    return max_people >= 3

if __name__ == "__main__":
    print(f'f("+-+++-+---") returns {f("+-+++-+---")}')
    print(f'f("+-+-+-+-") returns {f("+-+-+-+-")}')
    print(f'f("+-++-+--") returns {f("+-++-+--")}')
    print(f'f("+-++-++-+---") returns {f("+-++-++-+---")}')