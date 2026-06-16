#For finding sum of two integers we take two inputs from the user
#Taking input from the user
try:
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    if first_num < second_num:
        print(f"The difference of the two numbers is {second_num-first_num}")
    else:
        print(f"The difference of the two numbers is {first_num-second_num}")
except ValueError:
    print("Enter two valid integers. ")