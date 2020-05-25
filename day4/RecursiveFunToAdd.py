# write a recursive funtion to add 1 to 10 numbers

def sumOfNumbers(num):
    if num <= 1:
        return num
    else:
        return num + sumOfNumbers(num - 1)


print("Sum is :", sumOfNumbers(10))
