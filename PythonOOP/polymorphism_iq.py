# What is polymorphism in Python?
# Polymorphism means same interface, different implementations.
# In Python, it’s seen in:
# -Method overriding
# -Operator overloading
# -Duck typing
# ---------------------------------------------------------------
# What is method overriding? How is it different from overloading?
# Overriding → child class redefines a method from parent.
# Overloading → not directly supported in Python, instead we use default args / *args.
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

Child().greet() #Hello from Child
# ----------------------------------------------------------------------
# How does Python implement operator overloading?
# Using magic methods like __add__, __eq__, __len__, etc.
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Point(self.x+other.x, self.y+other.y)

p1, p2 = Point(1,2), Point(3,4)
print((p1+p2).__dict__)  # {'x': 4, 'y': 6}
# ----------------------------------------------------------------------
Can you overload methods in Python like Java/C++?
No direct support.
But we simulate with:
Default arguments.
*args/**kwargs

class Demo:
    def show(self,a=None,b=None):
        if a and b: print(a,b)
        elif a:print(a)
        else: print("Nothing")

Demo().show(10) #10
Demo().show(10,20) # 10 20
# ----------------------------------------------------------------------
# What is duck typing in Python?
# If an object implements required methods, type doesnt matter
class Duck:
    def speak(self):print("Quack")

class Person:
    def speak(self):print("Hello")

def call_speak(obj): obj.speak()

call_speak(Duck()) #Quack
call_speak(Person()) #Hello
# ----------------------------------------------------------------------
# How does polymorphism work with inheritance?
# Parent defines a method -> child overrides it -> we can cal the same method on different object 

# for animal in [Dog(), Cat()]:
#     animal.speak()
# ---------------------------------------------------------------------

# Give real-word example of operator overloading : 
# + → addition for numbers, concatenation for strings.

# * → multiplication for numbers, repetition for strings.

# in → membership check (x in list).

# -------------------------------------------------------------------
# What happens if you don’t implement __eq__ in a class?

# Object are compared by memory location , not values  

# class A:
#     pass 
# a1,a2=A(),A()

# print(a1==a2) #False (different addresses)
# -------------------------------------------------------------------
# What is method resolution order (MRO) and its role in polymorphism?
# MRO decides which Method Python calls when multiple classes define the same method 
# > Calculate using C3 linearization
# > Check with : Class.__mro__
# ---------------------------------------------------------------------
# Can polymorphism be achieved without inheritance in Python?
# Yes → via duck typing.
# As long as objects share the same method names, they can be used interchangeably without inheritance.