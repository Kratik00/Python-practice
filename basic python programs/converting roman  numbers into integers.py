#For converting roman numbers into integers we make a dictionary containing roman letters as key and integers as value
roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_num = input("Enter a roman number: ").upper() #Taking input from user and converting it into uppercase
total = 0
for i in range(len(roman_num)):
    if i > 0 and roman_dict[roman_num[i]] > roman_dict[roman_num[i-1]]:
        total += roman_dict[roman_num[i]] - 2 * roman_dict[roman_num[i-1]] #Subtracting the previous value as it was added before
    else:
        total += roman_dict[roman_num[i]] #Adding the value because no lower value is before it
print(f"The integer value of the roman number {roman_num} is: {total}")