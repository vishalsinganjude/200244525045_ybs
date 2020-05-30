'''
3. Write a program to implement multiple inheritance.
'''

class User:
    def __init__(self):
        self.name = input("Enter Your Name : ")
        self.age = int(input("Enter Your Age : "))

class Book:
    def __init__(self):
        self.bookID = int(input("Enter Book Id : "))
        self.bookName = input("Enter Book Name : ")
class Library(User, Book):
    def __init__(self):
        User.__init__(self)
        Book.__init__(self)
        self.libraryName = "Sharda Wachnalay!"

    def showAllInfo(self):
        print("\nName: ",self.name,"\nAge :",self.age)
        print("Library Name: ",self.libraryName)
        print("Book Id : ", self.bookID,"\nBook Name : ",self.bookName)

l = Library()
l.showAllInfo()