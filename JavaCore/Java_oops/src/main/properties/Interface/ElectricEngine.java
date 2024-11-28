package src.main.properties.Interface;

public class ElectricEngine implements Engine {
    
    public void start(){
        System.out.println("Electric engine is starting");
    }
    public void stop(){
        System.out.println("Electric engine is stopping");
    }
    public void acc(){
        System.out.println("Electric engine is accelerating");
    }
    
}
