# Diamond Problem : The diamond problem happens when due to multiple inheritence creates ambuigity
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C): #Diamond shape : D->(B,C)->A
    def show(self):
        print("D")
        super().show() 

d=D()
d.show()

#D->B->C->A
# super() respects the MRO and avoid infinite loop and duplicate classes 