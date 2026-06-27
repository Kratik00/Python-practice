#For finding those we use for loop to iterate every element and check with isstartswith() module.
#Defining a list 
food_list = ['burger', 'pizza', 'burschetta', 'burito', 'burino', 'paneer', 'paratha']
updated_list = []
for i in food_list:
    if i.startswith('b'):
        updated_list.append(i)
print(f"B words food items are: {updated_list}")