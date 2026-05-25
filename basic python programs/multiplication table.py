# For calculating the multiplication table of a number we can use a simple for loop to iterate through the numbers 1 to 10 and multiply them with the given number.
# Function to print multiplication table
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

# Taking input from the user
try:
    num = int(input("Enter a number to calculate its multiplication table: "))
    multiplication_table(num)
except ValueError:
    print("Please enter a valid integer.")