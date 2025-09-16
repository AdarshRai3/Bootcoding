#super is keyword that is used to in python that lets you call a parent's method from a child class. Useful of extending intead of replacing the behaviour

class Animal:
    def speak(self):
        print("Animal Makes Sound")

class Dog(Animal):
    def speak(self):
        super().speak() #call parent method
        print("Dog barks")

d = Dog()
d.speak()
