#For arranging countries in a dictionary we first take inputs then stored in a list and divide again in same letter starting and after that assign in dictionary
countries = input("Enter countries name by separating with a space: ").split()
dict_countries = {}
for i in countries:
    if i[0].upper() not in dict_countries:
        dict_countries[i[0].upper()] = [i]
    else:
        dict_countries[i[0].upper()].append(i)
print(dict_countries)