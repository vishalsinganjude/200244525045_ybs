'''
4. Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]
'''

lst1 = ['M','Na','i','Vis']
lst2 = ['y','me','s','hal']
result = [(i+j) for i, j in zip(lst1, lst2)]
print(result)