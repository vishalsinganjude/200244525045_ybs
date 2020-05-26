'''
1. Write a Python program to sort a list of elements using the bubble sort
Algorithm.
'''

def bubbleSort(lst):
    for i in lst:
        for j in range(len(lst)-1):
            if lst[j] >= lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst
lst = [8, 7, 6, 5, 4, 3, 2, 9]
print("Before Sort : ",lst)
print("After Sort the elements using bubble Sort :\n", bubbleSort(lst))
