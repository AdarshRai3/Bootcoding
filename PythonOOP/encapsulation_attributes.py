#__getattr__, __getattribute__, __setattr__,__setattribute__
#These are special methods to intercept attribute access
from typing import Any
# __getattr__ : Called only if attributes doesn't exist

class DynamicGetter:
    def __init__(self)-> None:
        self.existing = "I exist!"
    
    def __getattr__(self, name:str)-> str:
        return f"Attributes '{name}' not found , returning default"
    
obj = DynamicGetter()
print(obj.existing)
print(obj.non_existing)

# O/P: I exist!
# Attributes 'non_existing' not found , returning default

# #__getattribute__ : Called for every attribute access(be careful , can cause infinite recursion)
class Logger:
    def __init__(self)->None:
        self.value:int=42
        self.name:str="Adarsh"
        
    def __getattribute__(self, name:str)->Any:
        print(f"Accessing {name}")
        return super().__getattribute__(name)

obj=Logger()
print(obj.value)
print(obj.name)

# O/P:Accessing value
# 42
# Accessing name
# Adarsh

# #__setattr__: Intercept attribute assignment
class Tracker:
    def __setattr__(self, name:str, value:Any)->None:
        print(f"Setting {name}={value}")
        super().__setattr__(name,value)

obj = Tracker()
obj.x=100 #Log before setting 

# O/P: Setting x=100

# #__delattr__:Intercept attribute deletion
class Cleanup:
    def __delattr__(self, name:str)->None:
        print(f"Deleting {name}")
        super().__delattr__(name)

obj=Cleanup()
obj.attr="temp"
del obj.attr

# O/P : Deleting attr