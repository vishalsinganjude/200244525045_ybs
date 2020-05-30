'''
2. Write python program to check  that given number is valid mobile number or not?
'''
import re
mob = input("Enter Mobile Number : ")
matched = re.fullmatch("[7-9]\d{9}", mob)
if matched != None:
    print(mob, "is Valid Mobile number ..")
else:
    print(mob, "is not Valid Mobile number ..")