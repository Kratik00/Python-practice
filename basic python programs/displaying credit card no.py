#In this program we will display the credit card number in a masked format, showing only the last four digits.
#Taking input from user
cc_number = input("Enter your credit card number in same cc format(e.g. 1234 5678 9012 3456): ").replace(" ", "")
#Taking last four digits of credit card number
last_digits = cc_number[len(cc_number) - 4:]
#Creating masked format of credit card number
stars = "*" * 4 + " "
masked_cc_number = stars * 3 + last_digits
#displaying the masked credit card number
print(f"Your credit card number is: {masked_cc_number}")