# For Creating a complex number in Python we can use the built in complex() function or we can directly use the syntax a + bj where a is the real part and b is the imaginary part of the complex number. 
# Here is a simple python program to create a complex number:

# Get user input for real and imaginary parts of the complex number
try:
    real_part = float(input("Enter the real part of the complex number: "))
    imaginary_part = float(input("Enter the imaginary part of the complex number: ")) 
    # Create a complex number using the complex() function
    complex_number = complex(real_part, imaginary_part)
    print(f"The complex number is: {complex_number}")
except ValueError:
    print("Please enter valid numbers for the real and imaginary parts of the complex number.")