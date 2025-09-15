class Employee:
    def __init__(self, name:str, salary:float)-> None:
        self._name : str = name
        self._salary: str = salary
        
    @property
    def salary(self)->float:
        "Getter for salary(read only access)"
        return self._salary
    
    @salary.setter
    def salary(self,value:float)->None:
        "Setter with validation"
        if value<0:
            raise ValueError("Salary cannot be negative")
        self._salary=value
        
    @salary.deleter
    def salary(self)->None:
        "Delete the salary"
        print("Deleting the salary...")
        del self._salary
        
    
emp = Employee("Adarsh",6000)
print(emp.salary) #Calls Getter
emp.salary=12000 #Calls Setter
del emp.salary #Calls Deleter