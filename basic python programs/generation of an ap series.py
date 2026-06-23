#For generating an ap series we need three inputs first term, number of terms and common difference 
#Alternatively we can also done by taking last term instead of number of terms
#Taking input from the user
try:
    n = int(input("Enter how many terms you want to write: "))
    d = int(input("Enter the common difference: "))
    a = int(input("Enter the first term: "))
    print(f"The arithmatic sequence is : ", end="")
    for count in range(0, n):
        print(a+count*d, end=" ")
except ValueError:
    print("Please enter valid integers.")

#Alternative
try:
    l = int(input("Enter the last terms: "))
    print("The arithmatic sequence is: ", end="")
    count = 0
    while (a+count*d) <= l:
        print(a+count*d, end=" ")
        count += 1
except ValueError:
    print("Please enter valid integers. ")
#for count in (a, a+count*d, d) (can be done by also)