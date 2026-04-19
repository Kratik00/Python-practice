# For calculating gcd of two numbers we can use simple a while loop and check the greatest common divisor of two numbers.
# Here is a simple python program to calculate GCD of two numbers.
# Function for calculating GCD of two numbers.
def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2,num1 % num2
    return num1

# Get input from user
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")
except ValueError:
    print("Please enter valid integers.")