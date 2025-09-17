# Python follows “if it walks like a duck and quacks like a duck, it’s a duck” philosophy.
# It doesn’t care about type, only about whether the object implements required methods.
class Duck:
    def speak(self):
        print("Quack!")

class Human:
    def speak(self):
        print("Hello!")

def make_it_speak(obj):
    obj.speak()

make_it_speak(Duck()) #Quack!
make_it_speak(Human()) #Hello!

# No inheritence required --as long as an object has .speak() method , it works 
