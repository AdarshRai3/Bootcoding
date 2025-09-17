# What is inheritance in Python?
# Inheritence is used to reuse and extend the functionality of existing classes
# Supports single , multiple and multilevel inheritence
# -------------------------------------------------------------------------
# What is the difference between is-a and has-a relationship?
# Inheritence model is a example of is-a relationship: EX: Dog is a Animal
# Composition model is a example of has-a relationship. EX: Car has a engine
# ---------------------------------------------------------------------------
# How does method overriding work in Python?
# Child class defines a method with same name as parent->it overrides the parent method
# -------------------------------------------------------------------------
# What is super() used for?
# To call methods from the parent class safely, without hardcoding parent names.
# Follow MRO, avoid duplicate calls in multiple inheritence 
# ---------------------------------------------------------------------------
# What is the Diamond Problem? How does Python solve it?
# Ambiguity when multiple parents inherit from a common ancestor.
# Python solves it using C3 linearization (MRO)
# So each class is called onece in a deteministic order.
# ---------------------------------------------------------------------
# What is MRO (Method Resolution Order)?
# The order in which Python looks up methods when multiple inheritence is involved.
# Can be seen with ClassName.__mro__ or ClassName.mro()
# ----------------------------------------------------------------------
# How is MRO calculated in Python?
# Using C3 linearization algorihm
# Rules:Child class before parent, keep order of inheritence , no duplicates
# ----------------------------------------------------------------------
# Difference between super() and directly calling parent class method?
# super() respects MRO, so in multiple inheritance it ensures each class is called once.
# Direct parent call (Parent.method(self)) ignores MRO → may cause duplicate execution.
# ----------------------------------------------------------------------
# Can constructors (__init__) use super()? Yes 
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

b = B() 

# o/p: 
# A init 
# B init
# --------------------------------------------------------------------
# Difference between class variables and instance variables in inheritance?
# Class Variables : shared across all instances 
# Instance Variables : unique to each object
# In Inheritence m child can overrides parent's class variable.
# ----------------------------------------------------------------------