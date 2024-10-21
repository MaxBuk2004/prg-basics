def f(amount_to_pay):
    if amount_to_pay < 0:
        raise ValueError("Amount to pay must be non-negative.")
        
    coin_count = 0
    
    coin_count += amount_to_pay // 5
    amount_to_pay %= 5 
    
    coin_count += amount_to_pay // 2
    amount_to_pay %= 2
    
    coin_count += amount_to_pay
    
    return coin_count