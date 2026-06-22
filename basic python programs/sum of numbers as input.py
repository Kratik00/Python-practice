#For taking sum we can use a while loop and will add one by onee  
#Taking input from user
try:
    count = 0
    sum = 0
    n = int(input("Enter How many integers you want to add: "))
    while count < n:
        add_num = int(input(f"Enter {count+1} number: "))
        sum = sum + add_num
        count += 1
    print(f"The total sum of these numbers is {sum}.")

except ValueError:
    print("Please enter valid integers.")