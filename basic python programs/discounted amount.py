#For finding discounted amount first we take user input then calculate discount based on that and after that we subtract discount from original amount
#defining function 
def calculate_discounted_amount(amount):
    if amount <= 1000:
        discount_percent = 10
    elif amount > 1000 and amount <= 5000:
        discount_percent = 20
    elif amount > 5000 and amount <= 10000:
        discount_percent = 30
    elif amount > 10000:
        discount_percent = 50
    else:
        discount_percent = 0
    discount = amount*(discount_percent/100)
    discounted_amount = amount - discount
    return discounted_amount
#taking input from user
try:
    amount = float(input("Enter total amount of shopping: "))
    discounted_amount = calculate_discounted_amount(amount)
    print(f"Your total amount is {discounted_amount} after discount.")
except ValueError:
    print("Please enter a valid amount.")