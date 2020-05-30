'''
6. Write a python program to generate Fibonacci Numbers upto 100 using generator.
'''
def febo(num):
    a, b = 0,1
    while True:
        yield a
        a, b = b , a+b

num = int(input("Enter a Number : "))
for i in febo(num):
    if i > num:
        break
    print(i)



