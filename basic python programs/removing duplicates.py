#For removing duplicates from a list we can use a for loop to check each element and then can create a new list and then we can use .append() method to add and can also use set() method to remove duplicates
#Taking input from user
numbers = [int(c) for c in input("Enter a list of numbers separated by space: ").split()]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"The list after removing duplicates is: {unique_numbers}")
#---------------------------Method 2---------------------------
#Using set() module to convert the list to a set and then conver it back to a list to remove duplicates
unique = set(numbers)
print(f"The list after removing duplicates using set() method is: {list(unique)}")
