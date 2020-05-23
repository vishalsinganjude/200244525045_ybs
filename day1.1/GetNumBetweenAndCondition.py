'''
numbers between 2000 and 3201
make sure number is divide by 7 and not divide by 5
'''
lst = [i for i in range(2000, 3200+1) if i%7 == 0 and i % 5 != 0]
print(lst)