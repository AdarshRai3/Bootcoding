class Car:
    #Constructor
    def __init__ (self , brand:str ,model:str):
        self.brand:str = brand
        self.model:str = model
        
    def introduce(self)->None:
        print(f"Introducing you car of {self.brand} and it's name is {self.model}")
    def drive(self)->None:
        print(f"{self.brand} {self.model} is driving")
    

car1 = Car("Tesla","Model X")
car2 = Car("Toyata","Enevoa")

car1.introduce()
car2.introduce()
car1.drive()
car2.drive()