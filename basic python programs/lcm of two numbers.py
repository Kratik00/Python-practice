# For calculating LCM of two numbers we can use an infinite loop and check the least common multiple of two numbers.
# Here is a simple python program to calculate LCM of two numbers.
# function for calculating LCM of two numbers
def lcm(num1, num2):
    greater = max(num1, num2)
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            return greater
        greater += 1

# Get input from user
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = lcm(number1, number2)
    print(f"The LCM of {number1} and {number2} is: {result}.")
except ValueError:
    print("Please enter valid integers.")
