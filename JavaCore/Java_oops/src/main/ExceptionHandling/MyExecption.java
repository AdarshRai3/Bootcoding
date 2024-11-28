package src.main.ExceptionHandling;

public class MyExecption extends Exception{
    
    String message;
    public MyExecption(String message){
        super(message);
    }
}
//We can create our own exception by extends to Exception class.