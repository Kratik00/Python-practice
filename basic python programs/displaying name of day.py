#for displaying name of day we create a list of days and then we can take input from user and can access the list using index
#taking input from user
try:
    day_num = int(input("Enter a number (1-7) to get the corresponding day: "))
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(f"Your corresponding day is {days[day_num - 1]}")
except ValueError:
    print("Please enter a valid integer.")