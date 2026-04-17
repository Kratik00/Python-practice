# For converting age to seconds in Python we can use the formula. Age in second = Age in years * 365.25 * 24 * 60 * 60.
# Here is a simple pyhton program to convert age to seconds:
# Function to convert age to seconds

def age_to_seconds(age):
    total_seconds = age * 365.25 * 24 * 60 * 60
    return total_seconds

# Get user input for age
try:
    age = int(input("Enter your age in years: "))
    seconds = age_to_seconds(age)
    print(f"Your age in seconds is: {seconds}")
except ValueError:
    print("Please enter a valid age in years.")