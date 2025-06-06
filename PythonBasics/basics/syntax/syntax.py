import os
import sys

"""
This script demonstrates the use of type hints in Python.
a:int = 1
b:float = 3.14
c:str = "Hello, World!"
d:bool = True
e:list[int]=[1,2,3]
f:dict[str,int]={'a':1, 'b':2 , 'c':3}
g:tuple[int,str]=(1,"two")
h:set[int]={1,2,3}
"""
# -------------------------
"""This script demonstrates the use of if-elif-else statements in Python.

x:int = 5

if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")

"""
# --------------------------
# for i in range(10):
#     if i%2 == 0:
#         print(f"{i} is zero")
#     elif i%2 == 1:
#         print(f"{i} is one")
#     else:
#         print(f"{i} is neither zero nor one")
    
# --------------------------
# j: int = 10
# while j>0:
#     print(f"j is {j}")
#     j -= 1
# --------------------------

# def greet(name:str)-> str:
#     """
#     This function takes a name as input and returns a greeting message.
    
#     :param name: The name of the person to greet.
#     :return: A greeting message.
#     """
#     return f"Hello, {name}!"

# def list_operations(num : list[int])->list[int]:
#     """ This function takes a list of integers and returns a new list with each element incremented by 2"""
#     num = [i + 2 for i in num]
#     return num

# ----------------------------------------
# def dict_operations(d:dict[str,int])-> dict[str,int]:
#     """ This function takes a dictionary with string keys and integer values,
#     increments each value by 1, and returns the modified dictionary.
#     """
#     d["Hindi"] = 95
#     for subject, score in d.items():
#        print(f"{subject}:{score}")
       
#     return d
# -----------------------------------------      
# def greet(name: str = "Guest")-> str:
    
#     return f"Hello, {name}!"
# ------------------------------------------

# def sum_of_all(*args: int)->int:
#     total:int = 0
#     for i in args:
#         total +=i
    
#     return total
# -------------------------------------------
def print_info(*kwargs:Union[str, int, float]) -> None:
   
    for key, value in kwargs.items():
        print(f"{key}: {value}, type: {type(value)}")
        
      
         
    
if __name__ == "__main__":
    
    print("This script is designed to demonstrate Python syntax and type hints.")
    
    # num:list[int] = [1,3,5,7,9]
    
    # result:list[int] = list_operations(num)
    
    # print(f"Original list: {num}")
    # print(f"Modified list: {result}")
    
    # print(f"a: {a}, type: {type(a)}")
    # print(f"b: {b}, type: {type(b)}")
    # print(f"c: {c}, type: {type(c)}")
    # print(f"d: {d}, type: {type(d)}")
    # print(f"e: {e}, type: {type(e)}")
    # print(f"f: {f}, type: {type(f)}")
    # print(f"g: {g}, type: {type(g)}")
    # print(f"h: {h}, type: {type(h)}")
    # print(f"x: {x}, type: {type(x)}")
    
    # print(greet("Adarsh"))
    
    # scores : dict[str,int] = {"math":90, "science":85, "english":88}
    
    # dict_operations(scores) 
    
    # print(f"{scores}")  
    
    # s:str = "python is fun"
    # print(s.upper())
    # print(s.lower())
    # print(s.split())
    # print("fun" in s)
    
    #Tuple(immutable sequence of elements)
    # point:tuple[int,int]=(2,3)
    
    
    #Set(unique values only)
    # unique_nums: set[int] = {1, 2, 3, 4, 5}
    # unique_nums.add(6)
    # unique_nums.remove(2)
    # print(f"Unique numbers: {unique_nums}")
    
    # print(greet())
    
    # print(greet("Adarsh"))
    
    # print(f"Sum of all numbers: {sum_of_all(1, 2, 3, 4, 5)}")
