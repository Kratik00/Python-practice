#For converting a string into palindrome we can just reverse the string and cancatinate it with original string.
#Creating a function to convert string into palindrome
def convert_string_into_palindrome(a):
    reverse_string = a[::-1]
    return a + reverse_string

#Taking input from user
a = input("Enter a string to convert it into palindrome: ")
print(f"Your converted palindrome string is: {convert_string_into_palindrome(a)}")
#This program will work on both integer and string values just treat integer as string dont typecaste it while taking input from user otherwise indexing wont work.