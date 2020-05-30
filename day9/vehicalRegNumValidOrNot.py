'''
4. Write a python program to check given car registration number is valid Maharashtra state registration number or not?
'''
import re
vehicalNum = input("Enter Vehical Number : ")
matched = re.fullmatch("MH\d{2}[A-Za-z]{2}\d{4}", vehicalNum)
if matched != None:
    print(vehicalNum, "is Valid Vehical number..")
else:
    print(vehicalNum, "is not Valid Vehical number..")