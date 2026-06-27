#For calculating salary its like its in list containing the total working hours in whole week daywise and then we can use for loop to calculate the total working hours then multiply  it with hourly rate.
#Taking input from user
Working_hours = [int(x) for x in input("Enter theworking hours for each day and separate them by space: ").split()]
hourly_rate = int(input("Enter the hourly rate: "))
total_hours = sum(Working_hours)
salary = total_hours * hourly_rate
print(f"The total salary for the week is: {salary}")
