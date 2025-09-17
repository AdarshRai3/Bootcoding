#Method overriding : When a child class provides a new implememntation of a method already defined in its parent class

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks") #overriding

class Cat(Animal):
    def speak(self):
        print("Cat meows") #overriding

animals = [Dog(), Cat()]
for a in animals:
    a.speak()

# O/P:
# Dog barks
# Cat meows