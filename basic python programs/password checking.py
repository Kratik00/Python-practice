#in this file we check like in websites for setting password manner if password is same then same otherwise if vary in cases then tell check cases and after then if not both then its not same
#Take two inputs from the user
new_password = input("Enter your new password: ")
confirm_password = input("Enter same password again: ")
if new_password == confirm_password:
    print("Password is matching.")
elif new_password.casefold() == confirm_password.casefold():
    print("Password is same but differ in cases.")
else:
    print("Password is not matching please try again.")