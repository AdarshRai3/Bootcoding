#Multiple Inheritence : A class inherit from multiple parents 
class Wakable:
    def walk(self):
        print("walking...")


class Swimmable:
    def swim(self):
        print("swimming...")

class Duck(Walkable, Swimable): # Multiple inheritance
    def sound(self):
        print("Quack!")


duck=Duck()
duck.walk()  # from Walkable
duck.swim()  # from Swimmable
duck.sound() # from Duck