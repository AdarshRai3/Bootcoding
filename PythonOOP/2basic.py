class Person:
    
    #class-variable : a comman variable that shared among all classes
    species:str
    
    def __init__(self, name:str)->None:
        #instance variable(unique to each object)
        self.name=name
    
    #Instance Method
    def introduce(self,species)->None:
        print(f"Hello, I am a {species} and my name{self.name}")
        
#Object Creation
p1:Person=Person("Adarsh")
p2:Person=Person("AdRed")

p1.introduce("HomoSpaien")
p2.introduce("HomoSpaien")