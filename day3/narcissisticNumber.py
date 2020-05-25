'''
Example:
153 = 1 +  + 33
370 = 33 + 73 + 03
407 = 43 + 03 + 73.
There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
1634 = 1+64+34+44
8208 = 84+24+04+84
9474 = 94+44+74+44
'''
'''
def narcissistic(num):
    sum = 0
    v = num
    digits = [int(i) for i in str(num)] # int object not iterable thats why type cast to string
                                            # and store value in digit single-single digit
    lenDigits = len(digits)  #Get length of digits
    print("Length of num : ",lenDigits)
    while v > 0:
        rem = v % 10
        sum += rem ** lenDigits
        v //= 10
    if sum == num:
        print(num, "Number is narcissistic.")
        return True
    else:
        print(num, "Number is not narcissistic.")
        return False
num = int(input("Enter a Num :"))
print(narcissistic(num))
'''

sum = 0
num  = int(input("Enter number : "))
v = num
digits = [int(i) for i in str(num)] # int object not iterable thats why type cast to string
                                        # and store value in digit single-single digit
lenDigits = len(digits)  #Get length of digits
print("Length of num : ",lenDigits)
while v > 0:
    rem = v % 10
    sum += rem ** lenDigits
    v //= 10
if sum == num:
    print(num, "Number is narcissistic.")
else:
    print(num, "Number is not narcissistic.")
