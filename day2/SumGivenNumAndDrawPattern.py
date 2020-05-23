'''
suppose user enter 3 then
final output --- 1 + 2 + 3 = 6
'''
num = int(input("Enter a Num: "))
sum = 0
for i in range(1, num):
    sum += i
    print(i, "+ ", end="")
sum += num
print(num, "=", sum)