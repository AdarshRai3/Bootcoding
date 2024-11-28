package src.main.ExceptionHandling;

public class Main {
 public static void main(String[] args) {
     try {
         int a = 10;
         int b = 0;
         int c = divide(a,b);
         String name = "Ad";
         System.out.println(c);
         if(name.equals("Ad")){
            throw new MyExecption("This is my Exception");
         }
         throw new Exception("throw exception just for fun");
     } catch (ArithmeticException e) {
         System.out.println(e.getMessage());
     }
     catch(Exception e)
     {
         System.out.println(e.getMessage());
     }
     finally{
         System.out.println("Finally means no matter what happens, I will always run");
     }
     //this is Runtime Execption in the runtime exception it is Arthimetic Exception which is divide by zero.
 }
    static int divide(int a, int b) throws ArithmeticException{
        if(b==0){
            throw new ArithmeticException("Cannot divide by zero");
        }
       return a/b;
    }
}
//Error and Exception
//Error is non-recoverable, you cannot write the program with errors in it , it is usuallly cased due to lack of resources comman examples:Stack Overflow,Index out of Bound
//Exception is something that prevent the normal flow of the program,like dividing something by zero which is arthemetic execption and null pointer exception, we can actually recover from this we can put check for theses,it can be handled in java it is handled by throwable class which is parent of all exceptions and errors and Object class has throwable class as children and throwable class has error and exception class as it children.
//Exception are of two types: Checked and Unchecked Execptions
//Exception during compile time is checked Excetion and Runtime Exception is a unchecked Exception.
// we can use try catch block to handle the exceptions.
// we can explictly throw exception with the method itseld like we see in the divide(a,b) throws ArithmeticException{
//     if(b==0){
//         throw new ArithmeticException("Cannot divide by zero");
//     }
// }
// we can have multiple catch block for the specific Execptions 
//we can have our own Exceptions by using throw new Execption Name
// We can have multiple catch block for the specific Execptionsbt the order of specific Exception should be more to less.