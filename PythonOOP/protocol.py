from typing import Protocol

class Speaker(Protocol):
    def speak(self)->str:
        ...

class Dog:
    def speak(self)->str:
        return "Woof!"

class Cat:
    def speak(self)->str:
        return "Meow!"

def make_it_speak(animal:Speaker):
    print(animal.speak())


make_it_speak(Dog())
make_it_speak(Cat())

# When to use What :
# Use ABC when u=you want to enforce subclasses to implement certain method 
# Use Protocol/DuckTyping when you want flexibility and Pythonic style
# Use type hints with Protocol for better scalability in large system

