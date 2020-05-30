'''
5. Write a Python program to square and cube every number in a given list of integers using Lambda.
'''

lst = list(map(int, input().split()))
print("List :\n", lst)
squareList = list(map(lambda x: x*x, lst))
print("Square Of List :\n", squareList)
cubeList = list(map(lambda x: x**3, lst))
print("Cube of List :\n", cubeList)