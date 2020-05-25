# write two functions 1 for find first digit and 2 for find lastDigit
# eg : 1234 : first: 1, second: 4
#       1+4 = 5

def firstDigit(num):
    while num > 1 and num > 10:
        num //= 10  # iterate until first element
    return num  # return 1st digit


def lastDigit(num):
    return num % 10  # its return last digit


num = int(input("Enter Number : "))  # take input from user
print("Sum of first and last digit :", firstDigit(num) + lastDigit(num))
