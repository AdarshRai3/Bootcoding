package src.main.properties.Interface;

public class CDPlayer implements MediaPlayer{
    
    public void start(){
        System.out.println("CD player is starting");
    }
    public void stop(){
        System.out.println("CD player is stopping");
    }
    
}
