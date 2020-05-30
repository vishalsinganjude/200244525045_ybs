'''
5. Write a python program to decorate arithmetic operations.
'''
def arithmetic_operations(func):
    def operators(a, b):
        func(a, b)
        print("The product is :", a * b)
        print("The division is :", a / b)
        print("The remainder is :", a % b)

    return operators

print("This is a decorated function.")

@arithmetic_operations
def add_and_subtract(a, b):
    print("The addition is :", a + b)
    print("The subtraction is :", a - b)

add_and_subtract(25,10)
