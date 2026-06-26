#For finding the username and domain from email address we simply split the email address using .find() method and then we can access by slicing
#Taking input from user
email = input("Enter your email address: ")
#Finding the index of "@" symbol in email address
index = email.find("@")
#Accessing the username and domain using slicing
username = email[:index]
domain = email[index+1::]
print(f"Your username and domain from email address is: {username} and {domain}")
