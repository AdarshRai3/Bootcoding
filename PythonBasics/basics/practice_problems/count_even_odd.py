def is_even(n:int)-> bool:

    return n&1 ==0 

def count_even_odd(arr:list[int])->tuple[int,int]:

    even:int = 0
    odd:int  = 0

    for num in arr:
        if is_even(num):
            even+=1
        else:
            odd+=1
        
    return(even,odd)
        
          