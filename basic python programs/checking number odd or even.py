#For checking number is odd or even we need to divide the input with 2 
#Taking input from the user 
try:
    number = int(input("Enter the number: "))
    if number % 2 == 0:
        print(f"{number} is the even number.")
    else:
        print(f"{number} is the odd number.")
except ValueError:
    print("Enter the valid integer. ")