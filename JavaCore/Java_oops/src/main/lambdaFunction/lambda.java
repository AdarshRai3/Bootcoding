package src.main.lambdaFunction;
import java.util.*;

public class lambda {
    public static void main(String[] args) {
        ArrayList<Integer>arr = new ArrayList<>();
        for(int i =0;i<5;i++){
            arr.add(i+1);
        }

        arr.forEach((item)->{
            System.out.print(item*3+" ");
            System.out.println();
        });
        //item represents every element of the arraylist.
        //item is parameter 

        // Consumer<Integer> fun = (item)->System.out.println(item*2);
        // arr.forEach(fun);
        //this is internally consumer type works.
        
        Operation sum = (a,b)->a+b;
        Operation sub = (a,b)->a-b;
        Operation mul = (a,b)->a*b;
        Operation div = (a,b)->a/b;
        
        lambda myCalc = new lambda();
        
        System.out.println( myCalc.operate(10,5,sum));
        System.out.println(myCalc.operate(10,5,sub));
        System.out.println(myCalc.operate(10,5,mul));
        System.out.println(myCalc.operate(10,5,div));
 
    }

    private int operate(int a,int b, Operation op){
        return op.operator(a,b);
    }
    
}

interface Operation{
    int operator(int a, int b);
}
//forEach method takes the consumer dataType
//consumer is a datatype which has only one argument and return no result
// we know that consumer type take one argument and return no result, but if we want to use multiple arguments we can use interface like here we use first interface Operation{ int operator(int a, int b); you can clearly see that we have taken two parameter in operator method and use it like lambda function:Operator sum = (a,b)->a+b; } then to use it we created object lambda myCalc = new lambda(); System.out.println( myCalc.operate(10,5,sum));
