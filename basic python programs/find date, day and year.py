#For finding date, day and year wecan take input as dd/mm/yyyy and then we can split the string using .split() method and then we can access by list indexing.
#Taking input from user
date = input("Enter the date in dd/mm/yyyy format: ")
date_list = date.split("/")
day = date_list[0]
month = date_list[1]
year = date_list[2]
print(f"The date, month and year from the given input is: {day}, {month} and {year}")