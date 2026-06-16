#For checking eligibilty we can use logical operator "and" and check both cases minimum and maximum age for work
#Taking input from the user
try:
    age = int(input("Enter your age: "))
    if age >= 18 and age <=60:
        print("This person is elgible to work.")
    else:
        print("This person is not eligible.")
except ValueError:
    print("Please enter a valid age.")