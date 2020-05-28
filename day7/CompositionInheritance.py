'''
5. write any program  to achieve composition in Python
'''


class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getInfo(self):
        print("Car Name : ", self.name)
        print("Model Name : ", self.model)
        print("Color of Car : ", self.color)


class Employee:
    def __init__(self, empNo, empName, car):
        self.empNo = empNo
        self.empName = empName
        self.Car = car

    def empInfo(self):
        print("Employee Number : ", self.empNo)
        print("Employee Name : ", self.empName)
        print("\nCar Ki Information : ")
        self.Car.getInfo()


car = Car("Maruti 800", "A420", "Red-Black")
emp = Employee(420, "Nilesh Singal", car)
emp.empInfo()
