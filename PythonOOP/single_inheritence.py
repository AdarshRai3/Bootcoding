#Inheritence let us reuse and extends data members and member function to another

# Single Inheritence : One class inherits from one parent
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak() #Dog barks