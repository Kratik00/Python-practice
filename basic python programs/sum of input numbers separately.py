#For adding positive and negative numbers separately
try:
    count = 0
    pos_sum = 0
    neg_sum = 0
    n = int(input("Enter how many integers you want to add: "))
    while count < n:
        add_num = int(input(f"Enter {count+1} number: "))
        if add_num < 0:
            neg_sum = neg_sum + add_num
        else:
            pos_sum = pos_sum + add_num
        count += 1
    print(f"The total sum of positive integers is {pos_sum}")
    print(f"The total sum of negative integers is {neg_sum}")
except ValueError:
     print("Please enter valid integers.")