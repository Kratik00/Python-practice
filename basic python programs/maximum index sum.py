#For finding maximum index sum of two lists we can use for loop and then we can use .index() method to find index of each elemeent
#Declaring two lists
list1 = ["john", "alice", "suman", "karan", "rohit"]
list2 = ["alice", "john", "rohit", "suman", "karan"]
min_index = 10
for i in list1:
    ind = list1.index(i) + list2.index(i)
    if ind < min_index:
        min_index = ind
print(f"The minimum index sum of these lists is: {min_index}")
