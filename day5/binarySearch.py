'''
3. Write a Python program for Binary search.
'''

def binarySearch(lst, searchElement):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == searchElement:
            position = mid
            return position
        else:
            if searchElement < lst[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


lst = [8, 7, 6, 5, 4, 3, 2, 1, 9]
lst.sort()
print("Searching List :", lst)
searchElement = int(input("Enter a element to search : "))
a = binarySearch(lst, searchElement)
if a == -1:
    print("Element Not in list...")
else:
    print("Element Found at position %d." % (a))
