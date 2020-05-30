'''
3. Write python program to check  that given email address is valid or not ?
'''
import re
email = input("Enter Email Address : ")
matched = re.findall("\w[_.]*@[A-Za-z].com", email)
if matched != None:
    print(email, "is valid Email address.")
else:
    print(email, "not valid email address.")