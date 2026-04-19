# For calculating factorial we can use two methods one is iterative and second one is recursive method.
# Here is a simple python program to calculate factorial
# --------------------------METHOD 1-------------------------#
# Function for calculating factorial by iterative method
def factorial_by_iterative(n):
    i = 1
    result = 1
    # while n >= i:
    #     result *= i
    #     i += 1
    for i in range(1, n+1):
        result *= i
    return result
        
    
def factorial_by_recursive(n):
    if n == 0 or n == 1:
        result = 1
    else:
        result = n*factorial_by_recursive(n-1)
    return result

# Get input from user
try:
    num = int(input("Enter the number: "))
    fact1 = factorial_by_iterative(num)
    fact2 = factorial_by_recursive(num)
    print(f"The factorial of {num} is: {fact1} by iterative method.")
    print(f"The factorial of {num} is: {fact2} by recursive method.")
except ValueError:
    print("Please enter a valid integer")