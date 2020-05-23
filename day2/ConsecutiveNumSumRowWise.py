'''
    1
  3  5
 7  9  13
 ... so on consecutive odd numbers
suppose user gives row 2 then
3 + 5 = 8
so 8 is output
'''

def row_wise_sum(num):
    return num ** 3

num = int(input("Enter a Num: "))
print("Sum is ",row_wise_sum(num))