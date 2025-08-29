"""Singleton pattern ensures a class has only one instance during the whole execution of the program and provide a global point of execution to it
Good use cases : 
Database connections
Logging
Config
Thread pools 
Configurations

Problems with singleton design pattern :
Hidden dependencies 
Break SRP ( class is handleing business logic + also manages lifecycle)
Global State -> Tight Coupling -> Harder to Scale
"""
#Basic Singleton pattern 
from typing import Optional,ClassVar

class Singleton:
    _instance:ClassVar[Optional["Singleton"]] = None
    
    def __new__(cls)->"Singleton":
        if cls.instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        
        return cls._instance
    
    a=Singleton()
    b=Singleton()
    
# --------------------------------------------------------------------------------
import threading
from typing import Dict,ClassVar,Type,Any

class SingletonMeta(type):
    _instance = Dict[Type[Any],Any]={}
    _lock :ClassVar[threading.lock]=threading.Lock()
    
    
    def __call__(cls, *args:Any, **Kwargs:Any)->Any:
        if cls not in cls.instances:
            with cls._lock:
                if cls not in cls._instance:
                    cls._instance[cls]=super().__call__(*args,**kwargs)
        
        return cls._instance[cls]
    

class Database(metaclass=SingletonMeta):
    def __init__(self, conn:str)->None:
        self.conn = conn
        

db1 = Database("postgress://")
db2 = Database("postgress://")

#--------------------------------------------------------------------------
#In async pattern
import asyncio
from typing import ClassVar, Optional

class AsyncSingleton:
    _instance:ClassVar[Optional["AsyncSingleton"]]=None
    _lock:ClassVar[Optional[asyncio.Lock]]=None
    
    def __init__(self)->None:
        self.ready=False
        
    async def _init(self)->None:
        await asyncio.sleep(0.1)
        self.ready=True
    
    @classmethod
    async def get_instance(cls)->"AsyncSingleton":
        if cls._instance:
            return cls._instance
        if cls._lock is None:
            cls._lock=asyncio.Lock()
        async with cls._lock:
            if cls._instance is None:
                obj = cls()
                await obj._init()
                cls._instance = obj
        
        return cls._instance
    
    
async def main():
    a= await AsyncSingleton.getInstance()
    b= await AsyncSingleton.getInstance()
    print(a is b) #True
    
asyncio.run(main())