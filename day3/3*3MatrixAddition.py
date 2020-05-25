row = int(input("Enter Rows : ")) # enter How many rows u want in matrix
col = int(input("Enter Columns : ")) # enter How many columns u want in matrix
print("Enter Elements for matrix one : ")
firstMatrix = [[int(input()) for i in range(col)] for j in range(row)] # enter elements for 1st matrix
print("FirstMatrix :\n", firstMatrix) # print first matrix
print("Enter Elements for matrix second : ")
secondMatrix = [[int(input()) for i in range(col,)] for j in range(row)]  #enter elements for 2nd matrix
print("secondMatrix :\n", secondMatrix) #print second matrix
for i in range(len(firstMatrix)):
    for j in range(len(secondMatrix[0])):
        firstMatrix[i][j] += secondMatrix[i][j] # sum of 2 matrix and store in firstMatrix
print("Sum of 2 matrix is :\n", firstMatrix) # Print result