# create a function with default value if user not provide value then default value should be given

def showStudent(name,collegeName="VITA, Mumbai",id=1):
    print("Name :",name,"\nCollege name :",collegeName,"\nCollegeID :",id)
showStudent("Vishal")
print()
showStudent("Vishal","ICOER, Pune",52)