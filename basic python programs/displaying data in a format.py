#Display data in a format - Product Name......Price ------ Total - 25 Letters
#Taking 4 inputs 2 product name and 2 price tags respectively
try:
    product1 = input("Enter the first product name: ").title()
    price1 = int(input("Enter first product price: "))
    product2 = input("Enter the second product name: ").title()
    price2 = int(input("Enter second product price: "))
    length1 = 25 - len(product1) + len(str(price1))
    length2 = 25 - len(product2) + len(str(price2))
    str1 = product1.ljust(length1, ".")
    str2 = product2.ljust(length2, ".")
    print(str1+str(price1))
    print(str2+str(price2))
except ValueError:
    print("Please Enter valid products and prices. ")