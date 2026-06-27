#structure - [element1, occurenceof1, element2, occurenceof2 and so on]
#For arranging in this type of structure we can use for loop and then count variable 
#Defining a list
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd']
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
        a = list1.count(i)
        list2.append(a)
print(f"The list containing elements and occurence is: {list2}")
        