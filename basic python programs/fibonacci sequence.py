# For creating a Fibonacci sequence in Python we can simple use a loop to generat the Fibonacci numbers. The Fibonacci sequence is a series of numbers where each number is the sum of two preceding ones, using the formula f(n) = f(n-1) + f(n-2) with seed values f(0) = 0 and f(1) = 1.
# Here is the simple python program to create a Fibonacci sequence:
# Function to create a Fibonacci sequence:

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        print(a, end = ' ')
        sequence.append(a)
        a, b = b, a+b
    return sequence

# Get user input for the number of FIbonacci numbers to generate
try:
    n = int(input("Enter the number of Fibbonacci numbers to generate: "))
    if n < 0:
        print("Please enter a valid positive integer")
    else:
        sequence = fibonacci_sequence(n)
        print(f"\nThe Fibonacci sequence is: {sequence}")
except ValueError:
    print("Please enter a valid positive integer.")