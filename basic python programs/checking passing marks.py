#For checking we just add three subjects marks and use and logical operator to check if the marks are greater than equal to 45 or not
#Taking input from user
try:
    marks1 = int(input("Enter marks of first subject: "))
    marks2 = int(input("Enter marks of second subject: "))
    marks3 = int(input("Enter marks of third subject: "))
    if marks1 >= 45 and marks2 >= 45 and marks3 >= 45:
        print("Student is passed.")
    else:
        print("Student is failed")
except ValueError:
    print("Please enter valid marks.")