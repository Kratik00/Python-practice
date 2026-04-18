# For sorting three numbers we can just use swapping method. Like if a > b then a ,b = b, a
# Here is a simple python program to sort three numbers

#--------------------------------METHOD 01-------------------------------#
# Function for sorting three numbers
def sort_three_number1(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

#-------------------------------METHOD 02---------------------------------#
def sort_three_number2(a, b,c):
    mx = max(a, b, c)
    mn = min(a, b, c)
    md = a + b + c - (mx + mn)
    return mn, md, mx

# Get user input for all three numbers
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    sorted_numbers1 = sort_three_number1(num1, num2, num3)
    sorted_numbers2 = sort_three_number2(num1, num2, num3)
    print(f"Sorted numbers are: {sorted_numbers1}")
    print(f"Sorted numbers are: {sorted_numbers2}")
except ValueError:
    print("Please enter valid integers.")    