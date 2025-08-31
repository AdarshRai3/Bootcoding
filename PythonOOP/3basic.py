class Triangle:
    
    #class variable
    constant:int=0.5
    
    
    #class method(method that uses class variable)
    @classmethod
    def area(cls, height:int , base:int)->float:
        return cls.constant*base*height
    
    #static method(method that independent utility doesnot need any of the cls or self variabe means no dependency on class or instance variable)
    @staticmethod
    def add(x:int , y:int)->int:
        return x+y


p1=Triangle()
p2=Triangle()

area1:float=p1.area(12,5)
area2:float=p2.area(20,5)

print(f"Area of triangle are {area1} and {area2}")

    