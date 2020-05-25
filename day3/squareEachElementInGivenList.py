num = int(input("Enter A Num:"))
elements = []
for i in range(num):
    n = int(input())
    elements.append(n)
print("Original List :\n", elements)
squareEle = []
for i in elements:
    squareEle.append(i*i)
print("Square of elements:\n", squareEle)