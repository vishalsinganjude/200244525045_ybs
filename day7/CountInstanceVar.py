'''
4. Write a program to count how many reference variables in a program.
'''
import sys
class Demo:
    pass

d = Demo()
d1 = d
d2 = d1
d3 = d2
print("Number of instance Variables Are : ", sys.getrefcount(d))