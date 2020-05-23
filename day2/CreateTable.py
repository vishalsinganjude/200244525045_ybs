'''
user give num = 3
so print :
3 X 1 = 3
3 X 2 = 6 and so on
....
3 X 10 = 30
'''

num = int(input("Enter a Num: "))
for i in range(1,11):
    print(num,"X",i,"=",num*i)
