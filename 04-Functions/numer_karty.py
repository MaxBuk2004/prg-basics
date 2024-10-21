def hide(card_number):
    
    if len(card_number) != 16:
        raise ValueError("Credit card number must be 16 digits long.")
    
    masked_number = card_number[:2] + '*' * 10 + card_number[-4:]
    return masked_number