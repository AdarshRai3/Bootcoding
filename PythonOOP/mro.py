# Method Order Resolution(MRO) : when multiple classes are inherited , Python follows a specific order to look for methods 

class A:
    def show(self): print('A')

class B(A):
    def show(self): print('B')

class C(A):
    def show(self):print("C")

class D(B,C): #multiple inheritence
    def show(self): pass

d=D()
d.show() #O/P: B

# __mro__ : Every class has a __mro__ attribute(a tuple) that shows the order 
