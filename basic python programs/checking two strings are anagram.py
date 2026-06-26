#For checking two strings are anagram or not we can user split() method to split into list and then we can sorted() method to sort the list then we can compare both lists.
#Taking input from user
string1 = input("Enter first string: ").lower().replace(" ", "")
string2 = input("Enter second string: ").lower().replace(" ", "")
if sorted(string1) == sorted(string2):
    print(f"Strings '{string1} and '{string2}' are anagram.")
else:
    print(f"Strings '{string1} and '{string2}' are not anagram.")
print(sorted(string1))

