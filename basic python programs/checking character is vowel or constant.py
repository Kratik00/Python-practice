#for checking this we create a list containing all the vowels and then we check if the character is present in the list or not
#Taking input from user
try:
    character = input("Enter a character: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    if character in vowels:
        print("This character is a vowel.")
    else:
        print("This character is a constant.")
except ValueError:
    print("Please enter a valid character.") 