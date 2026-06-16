#For checking age eligibilty for casting vote we just need input age and then compare with your country's minimum age.
#Taking input from user
try:
    age = int(input("Enter your age: ")) 
    if age >= 18:
        print("Eligible for vost casting.")
    else:
        print("Not eligible. Age must be 18 or 18 plus.")
except ValueError:
    print("Enter valid age.")