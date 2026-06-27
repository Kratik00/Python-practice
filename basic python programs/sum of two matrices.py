#For finding sum of two matrices we use two loops 
#Defining two list(matrices)
matrix1 = ([1, 2, 3], [1, 2, 3], [1, 2, 3])
matrix2 = ([5, 6, 7], [5, 6, 7], [5, 6, 7])
matrix3 = []
for i in range(len(matrix1)):
    s = []
    for j in range(len(matrix2)):
        sum = matrix1[i][j] + matrix2[i][j]
        s.append(sum)
    matrix3.append(s)
print(matrix3)