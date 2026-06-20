#For checking admin access we take username as input and compare with admin usernames
#Taking input from user
try:
    username = input("Enter your username: ")
    if username == "john" or "smith":
        print("Authorised Access.")
    else:
        print("Unauthorised access.")
except ValueError:
    print("Please enter valid username.")