#For rearranging string based on cases first lowercase then uppercase we can use list method. 
#Taking input from user
string = input("Enter a string containing both cases: ").replace(" ", "")
#Creating two lists for storing lowercase and uppercase characters separately
lowercase_list = [c for c in string if c.islower()]
uppercase_list = [c for c in string if c.isupper()]
#sorting both lists in ascending order
lowercase_list.sort()
uppercase_list.sort()
rearranged_list = lowercase_list + uppercase_list
print(f"Your rearranged string letters is: {"".join(rearranged_list)}")