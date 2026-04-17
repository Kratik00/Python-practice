# Display the calculator menu

print("Welcome to the basic calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#TAKE INPUT FROM USER

CHOICE = input("Choose which type of calculation- 1/2/3/4: ")
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))

if CHOICE == "1":
    print(f"Result of the addition is {num1+num2}")
elif CHOICE == "2":
    print(f"Result of the subtraction is {num1-num2}")
elif CHOICE == "3":
    print(f"Result of the multiplication is {num1*num2}")
elif CHOICE == "4":
    if num2 ==0:
        print("Sorry this operation cant be executed.")
    else:
        print(f"Result of the division is {num1/num2}")

else:
    print("Wrong input..............!!")
