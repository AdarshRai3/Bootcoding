def add(a:int , b:int)->int:
    return a + b

print(add(2,3))


def reverse_string(s:str)->str:
    return s[::-1]

print(reverse_string("adarsh"))


def is_prime(n:int)->bool:
    if n<=1:
        return False
    
    for i in range(2,int(n**0.5),1):
        if n%i ==0:
            return False
    return True

print(is_prime(76))
print(is_prime(79))