#For checking leap year there is two condition one is year divided by 4 then its leap year and another one is if year divided by 100 then it have to be divided by 400 too for a leap year
#Taking input from the user
try:
    year = int(input("Enter an year: "))
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

except ValueError:
    print("Please enter a valid year.")