from basics.practice_problems.swap_numbers import swap_numbers
from basics.practice_problems.count_even_odd import count_even_odd
from basics.practice_problems.sum_of_two import sum_of_two
from basics.practice_problems.sum_of_list import sum_of_list
from basics.practice_problems.simple_caluclator import add,sub,mul,div
if __name__ == "__main__":

    """
    #use swap numbers
    a,b = map(int , input("Enter two numbers: ").split())
    x,y = swap_numbers(a,b)
    print("After swapping numbers:",x,y)
    
    #use count_even_and_odd
    arr=list(map(int,input("Enter a list of numbers: ").split()))
    even_count:int = 0
    odd_count:int = 0
    even_count,odd_count= count_even_odd(arr)
    print(f"Even numbers:{even_count}, Odd_numbers:{odd_count}")

    #sum of two numbers
    add:int = 0
    x:int
    y:int
    x,y = map(int,input("Enter two numbers: ").split())
    add:int = sum_of_two(x,y)
    print(f"sum of two number is :{add}")
    

    #List of sum of an array
    arr:list[int] = list(map(int, input("Enter the number in the array ").split()))
    add:int = sum_of_list(arr)
    print(f"Sum of all number in the list:{add}")
    """
    #use a simple calculator
    operations = {
        "add":add,
        "sub":sub,
        "mul":mul,
        "div":div
    }
    a:int
    b:int
    a,b = map(float,input("Enter two numbers: ").split())
    operation = input("Choose the operation you want:".strip().lower())

    if operation in operations:
        try:
           result:float = operations[operation](a,b)
           print(f"Result:{result}")
        except ValueError as e:
           print(f"Error:{e}")
    else:
        print("Invalid Operation")