'''
2. Write a Python program for sequential search (Linear search).
'''

def linearSearch(lst, searchElement):
    for i in range(len(lst)):
        if lst[i] == searchElement:
            return i
    return -1
lst = [8, 7, 6, 5, 4, 3, 2, 9]
print("Searching List : ", lst)
searchElement = int(input("Enter a Element to search : "))
position = linearSearch(lst, searchElement)
if position == -1:
    print("Element Not Found in list...")
else:
    print("Element Found at %d position..." % (position))
