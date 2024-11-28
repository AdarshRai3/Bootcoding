package src.main.properties.Interface;

public class Car implements Brake,Engine,MediaPlayer{
    
    @Override
    public void start(){
        System.out.println("Car is started");
    }
    @Override
    public void stop(){
        System.out.println("Car is stopped");
    }
    public void acc(){
        System.out.println("Car is accelerating");
    }
    public void brake(){
        System.out.println("Car is braking");
    }
    
}
