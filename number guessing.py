# importing modules
import random

#Generate a random number between 1 to 10
secret_number = random.randint(1, 10)
print("Welcome to the number guessing game. ")

attempts = 0
choice = input("Want to play? Tap Enter otherwise enter quit to exit: ").lower()
    
#loop until the user guesses the number or chooses to quit
while True:
    attempts += 1
    if choice == "quit":
        print("Thanks for playing! Goodbye.")
        break
    try:
        guess_num = int(input("Enter your Number: "))
    except ValueError:
        print("Enter only integer value")
    if guess_num == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess_num < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")  