class BaseConnection:
    def __new__(cls, *args,**kargs):
        print("Base Connection __new__->Allocating Memory")
        return super().__new__(cls) #calls object.__new__
    
    def __init__(self, name:str)->None:
        print(f"Base connection __init__ -> Initialising the base connection")
        self.name=name
        self.connected:bool=False
        
class DatabaseConnection(BaseConnection):
    def __new__ (cls, *args,**kwargs):
        print(f"Database Connection __new__->Before Base __new__")
        instance = super().__new__(cls)
        #delegate memory to Base Connection
        print("DataBaseConnection __new__->After Base __new__")
        return instance        
        
    def __init__(self,db_name:str)->None:
        print("Database Connection __init__->Before Base __init__")
        super().__init__(db_name)
        self.connected:bool = True
        print("Database Connection __init__->Before Base __init__")
        
    def __str__(self)->str:
        return f"Database connection to {self.name}"
    
    def __repr__(self)->str:
        return f"Database Connection (name = {self.name!r},connected={self.connected!r})"
    
    def __del__(self)->None:
        if self.connected:
            print(f"__del__ -> Closing Database connection to {self.name}")
            

db=DatabaseConnection("UpstashRedis/CrazyMonekey")

print(str(db)) #calls __str__ : for users
print(repr(db)) #call __repr__:for developers

del db #explicitly delete object and free memory by triggering __del__
        