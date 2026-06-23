#For finding prime numbers 1 to 100 we use nested loop
count = 0
print("The prime numbers between 1-100 are: ", end="")
for i in range(2, 101):
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end=" ")
    count = 0
