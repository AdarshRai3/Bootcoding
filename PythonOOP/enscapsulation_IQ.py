# Q1. What is encapsulation in Python?
# A: Encapsulation is the process of hiding internal state(data) and providing controlled access via methods / properties

# Python don't enforce strict access modifiers but uses :
#  public : no underscore
#  protected :_single_underscore
#  private: __double_underscore

class A:
    def __init__(self)->None:
        self.public ="public"
        self._protected="protected"
        self.__private="private"
# ----------------------------------------------------------------
# Q2.What is the difference between _var and __var?
# Ans: _var : protected (convention , not enforced)
# __var:private:Python applies name mangling-> _ClassName__var
class Test:
    def __init__(self)->None:
        self._x=1 #Protected 
        self.__y=2 #Private
    
t=Test()
print(t._x) #Works but discouraged
print(t._Test__y) #access private with mangling
# ------------------------------------------------------------------
# Q3. Can we make attributes truly private in Python?

# No ❌. Even with __private, attributes can be accessed using name-mangling. Encapsulation in Python is by convention, not by force.
# ---------------------------------------------------------------------
# Q4. What is the use of @property in Python?
# @property makes a method behave lie an attribute. Useful for controlled access without breaking API

class Employee:
    def __init__(self, salary:float)->None:
        self._salary = salary
        
    @property
    def salary(self)->float:
        return self._salary

    @salary.setter
    def salary(self,value:float)->None:
        if value<0:
            raise ValueError("Salary cannot be negative")
        self._salary=value
# --------------------------------------------------------------------------------------------
# Q5. Difference between __getattr__ and __getattribute__?
# __getattr__: Called only if attribute not found.
# __getattribute__: Called for every attribute access.

class Test:
    def __getattr__(self, name:str):
        return f"{name} not found"
    
    def __getattribute__(self, name:str):
        print(f"Accessing{name}")
        return super().__getattribute__(name)

t=Test()
print(t.exists)

# -------------------------------------------------------------------------------------------
# Q6. When to use __setattr__?
# To intercept and control assignment(useful for logging, validation, immutability)
class Immutable:
    def __setattr__(self, name, value):
        if hasattr(self,name):
            raise AttributeError("Cannot modify attribute")
        super().__setattr__(name,value)

obj=Immutable()
obj.x=10
# obj.x=20 #Error
# --------------------------------------------------------------------------------------------
# Q7. What is the purpose of __delattr__?
# It controls delation of attributes
class MyClass:
    def __delattr__(self,name):
        print(f"Deleting {name}")
        super().__delattr__(name)

obj=MyClass()
obj.attr="test"
del obj.attr #Logs delation
# -------------------------------------------------------------------------------------------
# Q8. Why use @property instead of getter/setter methods?

# Cleaner syntax (emp.salary vs emp.get_salary()).
# Backward compatibility → can convert existing attributes into controlled properties without changing code.
# ---------------------------------------------------------------------------------------------
# Q10. How can encapsulation improve maintainability?

# Hides implementation details.

# Allows validation/logging without changing interface.

# Makes classes robust and future-proof.
class Temperature:
    def __init__(self, celsius:float)->float:
        self._celsius=celsius
    
    @property
    def fahrenheit(self)->float:
        return (self._celsius *9/5)+32