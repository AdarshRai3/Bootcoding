Operator overloading : Operators are implemented using dunder methods(__add__, __eq__, __len__)

class Vector:
    def __init__(self,x,y):
        self.x,self.y=x,y
    
    def __add__(self,other)
        return Vector(self.x + other.x, self.y+other.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"

v1 = Vector(2,3)
v2= Vector(4,5)
print(v1+v2) #(6,8)


class Book:
    def __init__(self , title ,pages):
        self title, self.pages= title , pages
    
    def __eq__(self, order):
        return self.pages==other.pages

b1=Book("Book A",300)
b2=Book("Book B",300)

print(b1==b2) #True, since we have overrided the equal method not we are comparing pages , not memory addresses 

class Library:
    def __init__(self,book):
        self.book = book
    
    def __len__(self):
        return len(self.book)

lib= Library(["Book A", "Book B" , "Book C"])
print(len(lib)) #3