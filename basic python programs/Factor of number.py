# For calculating factors of a number we can use a while loop and divide by every number till square root of n and if remainder is zero then its a factor of that number.
# Here is a simple python program to calculate Factors of a number.
# Function to calculate factors
def factor(num):
    factors = []
    i = 1
    while i * i < num:
        if num % i == 0:
            factors.append(i)
            if num != i*i:
                factors.append(num//i)
        i += 1
    return sorted(factors) 

# Get input from user
try:
    number = int(input("Enter the number: "))
    print(f"Factors of the {number} is: {factor(number)}")
except ValueError:
    print("Please enter a valid positive number.")