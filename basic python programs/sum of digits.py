# For calculating sum of digits of a number we can use a while loop take remainder every time dividing by 10.
# Here is a simple python program to calculate sum of digits of numbers.
# Function to calculate sum of digits
def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum = number % 10 + sum
        number //= 10
    return sum

# Get input from user
try:
    num = int(input("Enter the number: "))
    total_sum = sum_of_digits(num)
    print(f"The sum of digits is: {total_sum}")
except ValueError:
    print("Please enter a valid number.")

