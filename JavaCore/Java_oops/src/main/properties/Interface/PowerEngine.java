package src.main.properties.Interface;

public class PowerEngine implements Engine{
    
    public void start(){
        System.out.println("Power engine is starting");
    }
    public void stop(){
        System.out.println("Power engine is stopping");
    }
    public void acc(){
        System.out.println("Power engine is accelerating");
    }
}
