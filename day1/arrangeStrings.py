# Q3 Arrange String characters such that lowercase letters should come first

input_String = "PyNaTive"
# alpha = input_String.split()
l_case = []
u_case = []
for i in input_String:
    if i.isupper():
        u_case.append(i)
    else:
        l_case.append(i)

str_sort = ''.join(l_case+u_case)
print("Original String :",input_String)
print("arranging characters giving precedence to lowercase letters:\n",str_sort)