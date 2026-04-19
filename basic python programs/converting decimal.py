# For converting decimal into binary, octet and hexadecimal we can just use basic methods.
# Here is a simple python program to convert decimal.
# Function for converting Decimal to Binary
def decimal_to_binary(num):
    result = ""
    while num > 0:
        result = str(num%2) + result
        num //= 2
    return result

# Function for converting Decimal to Octet
def decimal_to_octet(num):
    result = ""
    while num > 0:
        result = str(num%8) + result
        num //= 8
    return result 

# Function for converting Decimal to Hexadecimal
def decimal_to_hexadecimal(num):
    result = ""
    hex_range = "0123456789ABCDEF"
    while num > 0:
        result = hex_range[num%16] + result
        num //= 16
    return result

# However we can also use built-in python functions to convert decimal into binary, octet and hexadecimal.
# For Binary
print(bin(10))

# For Octal
print(oct(10))

# ForHexadecimal
print(hex(10))

# Taking input from user
try:
    decimal_number = int(input("Enter a decimal number: "))
    print(f"The binary number of {decimal_number} is: {decimal_to_binary(decimal_number)}")
    print(f"The octal number of {decimal_number} is: {decimal_to_octet(decimal_number)}")
    print(f"The hexadecimal number of {decimal_number} is: {decimal_to_hexadecimal(decimal_number)}")
except ValueError:
    print("Please enter a valid decimal number.")
    