#For concatenating all digits present in a list we can use for loop to convert each element to string then we can add them to a new string 
num = [3, 4, 6, 5, 7, 9, 8, 2,1]
number = ""
for i in num:
    number = number + str(i)
print(f"The concatenated number is: {number}")
#-----------------------------Method 2---------------------------
#using list comprehension to convert each elements into string and then using join() method to concatenate them
for i in num:
    number = "".join(str(i) for i in num)
print(f"The concatenated number using join() method is: {number}")