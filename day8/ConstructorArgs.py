'''
1. Write a program to implement Constructor with Variable Number of Arguments.
'''
class Demo:
    def __init__(self,*args):
        print(sum(args))

d1 = Demo(1,2)
d2 = Demo(1,2,3,4,5)

# Keyword Arguments work as a dictionary
class Demo2:
    def __init__(self, **kwargs):
        for i, j in kwargs.items():
            print(i,":",j)

da = Demo2(a = 11, b = 19)