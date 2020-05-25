# write a function to return unique elements in the list

def uniqueElements(lst):
    uniqueList = []
    for i in lst:
        if i not in uniqueList:
            uniqueList.append(i)
    print("Unique elements in a list :",uniqueList)

lst = [11,22,22,33,33,33,44,55,55,66]
uniqueElements(lst)