#For checking prime we simply take number input and check by for loop 
#Taking input from user
try:
    num = int(input("Enter the number: "))
    count = 0
    for n in range(1, num+1):
        if num % n == 0:
            count += 1
    if count == 2:
        print("This number is prime. ")
    else:
        print("This number is not prime.")
except ValueError:
    print("Please enter valid integers")