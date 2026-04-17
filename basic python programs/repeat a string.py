# For repeting a string in Python we use a multiplication operator. Syntax for repeating a string is: string = string * n where string is the string you want to repeat and n is the number of times you want to repeat.
# Here is a simple python program to repeat a string:
# Function to repeat a string

def repeat_string(string, n):
    repeated_string = string * n
    return repeated_string

#Get user input for string and number of times to repeat
try:
    string = input("Enter the string you want to repeat: ")
    n = int(input("Enter the number of times you want to repeat the string: "))
    result = repeat_string(string, n)
    print(f"The repeated string is: {result}")
except ValueError:
    print("Please enter a valid number for the number of times to repeat the string.")