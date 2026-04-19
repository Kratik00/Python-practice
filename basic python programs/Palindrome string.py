# This method is used to check any data type where it is palindrome or not !
# New Method and Easy you can go through the slicing methhod as your wish  

def check_palindrome(name):
  reverse_name = name[::-1]
  if name == reverse_name:
    print(f"Yes {name} is palindrome")
  else :
    print(f"{name} is not an palindrome)")

try:
  name = input("Enter the string: ")
  check_palindrome(name)
except ValueError:
  print("Please enter a valid string to check palindrome.") 
