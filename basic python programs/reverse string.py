# For reversing a string we can do by two methods. First one is simple loop method and other one is just use indexing method.
# Here is a simple python program to reverse string.
# Function to reverse string
def reverse_string(text):
    reverse = ""
    i = len(text) - 1
    # for ch in text:
    #     reverse = ch + reverse
    while i >= 0:
        reverse = reverse + text[i]
        i -= 1
    return reverse

try:
    string = input("Enter the string: ")
    print(f"The reversed string is: {reverse_string(string)}")
    print(f"The reversed string is: {string[::-1]}")   #BY INDEXING METHOD
except ValueError:
    print("Enter a valid string to reverse.")
