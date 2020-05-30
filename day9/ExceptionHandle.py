'''
1. Write a function to compute divide by zero and use try/except to catch the exceptions.
'''


def divide(num1, num2):
    try:
        num3 = num1 / num2
        print("result : ", num3)
    except Exception as e:
        print("Exception raised : ", e)
    finally:
        print("End of Program...Until then Happy Coding")


num1 = int(input("Enter 1st num : "))
num2 = int(input("Enter 2st num : "))
divide(num1, num2)
