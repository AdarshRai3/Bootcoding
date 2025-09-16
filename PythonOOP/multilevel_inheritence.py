# Multilevel Inheritence: A chain of inheritence

class Animal:
    def speak(self):
        print("Animal speak")


class Mammal(Animal):
    def feed(self):
        print("feeds milk")

class Dog(Mammal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.feed() #Inherited from Mammal
d.speak() #Overriden in Dog