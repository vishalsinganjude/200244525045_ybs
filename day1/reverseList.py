# Q1. Given a number count the total number of digits in a number

lst = [10,20,30,40,50]
count = 0
for i in range(len(lst)-1, -1, -1):
    count +=1
    print(lst[i])
print("Count is : ", count)