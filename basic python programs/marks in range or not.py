#For checking marks in range of 0-100 or not we have to use logical operator AND.
#Taking input from user
try:
    marks = int(input("Enter your obtained marks: "))
    if marks >= 0 and marks <= 100:
        print("Marks are valid for particular subject.")
    else:
        print("Marks are invalid please enter within the range of 0-100.")
except ValueError:
    print("Please enter a valid integer.")
    