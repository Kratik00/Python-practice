#For removing all punctuations from a string we can use string.punctuation and then we can ue for loop to check each punctuation and then wecan use .replace() method
#Taking input from user
import string
text = input("Enter a string containing punctuation: ")
clean_text = "".join([s for s in text if s not in string.punctuation])
print(clean_text)