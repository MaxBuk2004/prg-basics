number_of_products = int(input("Enter the number of products purchased: "))
product_price = float(input("Enter the product price: "))

if number_of_products > 2:
    full_price_amount = 2 * product_price
    discounted_products = number_of_products - 2
    discounted_price_amount = discounted_products * (product_price * 0.75)
    total_amount = full_price_amount + discounted_price_amount
else:
    total_amount = number_of_products * product_price
    
print(f"Amount to pay: {total_amount:.2f}")