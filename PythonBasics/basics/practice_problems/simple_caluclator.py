def add(a:float ,b:float) ->float:
    return a+b

def sub(a:float , b:float)-> float:
    return a-b

def mul(a:float, b:float)->float:
    return a*b

def div(a:float, b:float)->float:
    if(b==0):
        raise ValueError("Cannot be divided by zero")
    
    return a/b

