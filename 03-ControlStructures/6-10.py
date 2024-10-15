previous_price = float(input('Enter the previous product price: '))
current_price = float(input('Enter the current product price: '))

price_reduction_percentage = ((previous_price - current_price) / previous_price) * 100

if price_reduction_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {round(price_reduction_percentage, 2)}%")
else:
    print("No need to buy. The price hasn't decreased enough.")