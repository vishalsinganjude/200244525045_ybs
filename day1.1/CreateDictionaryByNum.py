'''
Create a Dictionary
eg if user enter = 4
so we get
output = { 1:1, 2:4, 3:9, 4:16 }
'''
n = int(input("Enter Number:"))
d = dict()
i = 1
while n >= 1:
    d[i] = i*i
    n -= 1
    i += 1
print(d)
