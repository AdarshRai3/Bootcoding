#Encapsulation: Enclosing the data member and member fuction with the class and controllig their access using access specifiers
from typing import Any

class BankAccount:
    def __init__(self, owner:str, balance:float)->None:
        #Public attribute (anuone can access)
        self.owner:str=owner
        
        #Protected attribute()(cannot be accessed outside the class and suclass)
        self._balance:float=balance
        
        #Private attribute( name margling : _BankAccount.__pin)
        self.__pin:int=1234
    
    def deposit(self, amount:float)->None:
        "Public Method"
        self._balance+=amount
    
    def get_balance(self)->float:
        "Public Method that safely returns balance"
        return self._balance
    
    def __verify_pin(self,pin:int)->bool:
        "Private Method"
        return self.__pin==pin
    
    #Usage
    account = BankAccount("Adarsh",1000.0)
    
    print(account.owner)#Public
    print(account._balance) #By convention : protected 
    print(account.__pin) #Error:private
    print(account._BankAccount.__pin) #Accessible(name mangled)
        
        
