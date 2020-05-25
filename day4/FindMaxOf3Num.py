def maxNumber(n1, n2, n3):
    if n1 > n2 and n1 > n3: #check max num
        return n1
    elif n2 > n1 and n2 > n3: #check max num
        return n2
    else:
        return n3
print(maxNumber(6,2,4)) # function call and pass values and print max number