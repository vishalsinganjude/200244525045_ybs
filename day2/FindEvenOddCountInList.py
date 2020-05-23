lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
oddCount = 0
evenCount = 0
for i in lst:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
print("Odd numbers count : ",oddCount)
print("Even numbers count : ",evenCount)
