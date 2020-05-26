'''
5. Iterate a given list and check if a given element already exists in a dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}
expected output : [47,64,37,76]
'''

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {"Vishal": 47, "Shankar": 37, "Nilesh": 83}
result = [i for i in roll_number if i in sampledict.values()]
print(result)
