#For checking gender ask from the user whats his/her gender simply and tell by print function
#Taking input from the user
gender = input("What's your gender? ").lower() #lower() function use for convrting all characters in a string into lower case
if gender == "male":
    print("User is male.")
elif gender == "female":
    print("User is female.")
else:
    print("Enter a valid gender.")