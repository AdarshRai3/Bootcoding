# Python provides abc(absract base class) module to define abstract class and method 
# key points 
# Abstract classes cannot be instantiated 
# Abstract methods must be implemented in subclasses 
# Use @abstractmethod decorator

from  abc import ABC , abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    

class Rectangle(Shape):
    def __init__(self , width , height):
        self.width= width
        self.height=height
    
    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2*3.14*self.radius

shapes=[Rectangle(10,20),Circle(5)]

for shape in shapes:
    print(f"{shape.__class__.__name__}-Area:{shape.area()} | Perimeter:{shape.perimeter()}")

# Shape defines what operation must exist (area , perimeter)
# Rectangle and Circle define how those operation are done