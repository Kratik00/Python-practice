#For finding maximum number we assign a variable max and by loop and if statement compare with inputs if previous input is greater than previous one then assign max otherwise same
#Taking input from user
try:
    count = 0
    max = 0
    n = int(input("Enter how many positive integers you want to compare: "))
    while count < n:
        num = int(input(f"Enter {count+1} positive number: "))
        if num > max:
            max = num
        count += 1
    print(f"The maximum number among all the inputs is {max}.")
except ValueError:
    print("Please enter valid positive integers.")