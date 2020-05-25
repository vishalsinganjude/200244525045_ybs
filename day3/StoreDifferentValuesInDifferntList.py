elements = ['Hii', 32, 45.4, "vishal", 21.21, 22]
lstInt = [x for x in elements if isinstance(x, int)]
print(lstInt)
lstStr = [x for x in elements if isinstance(x, str)]
print(lstStr)
lstFloat = [x for x in elements if isinstance(x, float)]
print(lstFloat)