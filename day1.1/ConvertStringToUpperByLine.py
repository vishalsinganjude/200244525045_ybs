'''
User ask how many line u r enter
if u give 2 then
its ask enter a string 2 times
eg: Hi I am Vishal
    I am From India.
so we get output like this :
    HI I AM VISHAL
    I AM FROM INDIA.
'''
userInput = int(input("Enter Num of Lines : "))
par = []
for i in range(userInput):
    str = input("Enter a String: ")
    par.append(str.upper())
print("String in uppercase : ")
if par:
    print('\n'.join(par))

