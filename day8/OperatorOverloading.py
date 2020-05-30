'''
4. Write a program to implement operator overloading in python.
'''

class Operator:
    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        return self.num * other.num

a1 = Operator(20)
a2 = Operator(3)
print("Multiplication Of two Numbers : ", a1 * a2)