'''
# Create below pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

num = int(input("Enter a Num: "))
for i in range(1,num+1):
    for j in range(i):
        print(i, end=" ")
    print()

