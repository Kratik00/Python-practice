# For checking a number whether is palindrome number or not we can use two methods first one is string method and second one is integer method.
# Here is a simple python program to check palimdrome number
# Functions to check palindrome 
# -------------------------METHOD 1------------------------#
def check_palindrome_number1(a):
    reverse_string = a[::-1]
    if reverse_string == a:
        return True
    else:
        return False

# -------------------------METHOD 2-------------------------#
def check_palindrome_number2(a):
    rev = 0
    original = a
    while a > 0:
        digit = a%10
        rev = rev * 10 + digit
        a = a//10 # You can simply write a //= 10 
    return rev == original
        
# Get user input for checking palindrome numbers
try:
    num = input("Enter the number: ")
    check1 = check_palindrome_number1(num)
    check2 = check_palindrome_number2(int(num))
    if check1:
        print("Yeah! Number is palindrome")
    else:
        print("Invalid input")
    if check2:
        print("Yeah! Number is palindrome")
    else:
        print("Invalid input")
except ValueError:
    print("Please enter a valid integer.")

