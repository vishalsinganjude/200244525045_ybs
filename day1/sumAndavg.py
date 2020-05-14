# Q4. Given a string, return the sum and average of the digits that appear in the string, ignoring all other
#characters
import re
str = "English = 78 Science = 83 Math = 68 History = 65"
lst = [int(i) for i in re.findall(r'\b\d+\b',str)] # \b is use for space and \d is for digit
len_lst = len(lst)
total = 0
for i in lst:
    total += i
percentage = total/len_lst
print("sum is", total)
print("Percentage is", percentage)