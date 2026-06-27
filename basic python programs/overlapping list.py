#For finding overlapping elements in two lists we can use for loop and if any element is present in both lists then we can append that element to a new list.
#Defining two lists
list1 = [1, 4, 7, 34, 9, 12]
list2 = [4, 9, 45, 12, 6, 8, 9]

overlapping_list = []
for i in list1:
    if i in list2:
        overlapping_list.append(i)
print(f"The overlapping list is: {overlapping_list}")