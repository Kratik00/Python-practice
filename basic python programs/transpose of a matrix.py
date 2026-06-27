#For finding the transpose of matrix we use two loops
#Defining a list[matrix]
matrix = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
transpose_matrix = []
for i in range(len(matrix)):
    temp = []
    for j in range(len(matrix)):
        a = matrix[j][i]
        b = temp.append(a)
    transpose_matrix.append(temp)
print(transpose_matrix)