# Count local variables

#1
x = "hii"
def localVarCount():
    a, b, c, d = "Java", 10, "C", 2.5

print("Total local variables : ", localVarCount.__code__.co_nlocals)

#2
x = "Python"
def localVarCount():
    a, b, c, d, e = "Java", 10, "C", 2.5, 7
    return len(locals())
print("Total local variables : ", localVarCount())
